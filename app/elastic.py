from elasticsearch import AsyncElasticsearch
import os
from lxml.etree import _Element
from asyncio import gather, create_task, all_tasks, current_task
from elastic_transport import ObjectApiResponse
from database import add_similar_products


async def get_es_connection() -> AsyncElasticsearch:
    return AsyncElasticsearch(
        hosts=['http://elasticsearch:9200'],
        basic_auth=("elastic", os.getenv('ELASTIC_PASSWORD')),
        maxsize=int(os.getenv('AMOUNT_OF_CONCURRENT_PRODUCTS')),
        max_retries=5,
        retry_on_timeout=True
    )


async def indexing_to_es(elastic_con: AsyncElasticsearch, offer: _Element,
                         uuid_object, category: str):
    await elastic_con.index(index=category, document={
        'uuid': uuid_object,
        'title': offer.findtext('name'),
        'description': offer.findtext('description'),
        'brand': offer.findtext('vendor'),
        'seller_name': offer.findtext('vendor'),
    })


async def get_chunk_of_products(elastic_con: AsyncElasticsearch,
                                category: str, pool):
    search_after_value = ''
    while True:
        response: ObjectApiResponse = await elastic_con.search(
            index=category,
            body={
                "search_after": [search_after_value],
                "sort": [
                    {"uuid.keyword": "asc"}
                ]
            },
            size=int(os.getenv('AMOUNT_OF_CONCURRENT_PRODUCTS')))

        products: list[dict | None] = response['hits']['hits']
        if not products:
            break
        search_after_value = products[-1]['sort'][0]

        print(f'Got {len(products)} products, start finding similar...')
        create_task(process_similar_products(elastic_con, category,
                                             products, pool))
    all_tasks_ = all_tasks()
    all_tasks_.remove(current_task())
    print(f'Waiting the last {len(all_tasks_)} tasks to finish...')
    await gather(*all_tasks_)


async def process_similar_products(elastic_con, category: str,
                                   products: list[dict], pool):
    all_similar: list[dict[str, list[str]]] = await gather(
        *(get_similar(elastic_con, category, product)
          for product in products))
    await add_similar_products(pool, *all_similar)
    print('Similar products have been found and added to database')


async def get_similar(elastic_con: AsyncElasticsearch, category: str,
                      product: dict):
    similar: tuple[str, ObjectApiResponse] = (
        product.get('_source')['uuid'],
        await elastic_con.search(
            index=category,
            body={
                "query": {
                    "more_like_this": {
                        "fields": list(product.get('_source')),
                        "like": [
                            {
                                "_id": product.get('_id'),
                                "_index": category
                            }
                        ],
                        "min_term_freq": 1,
                        "max_query_terms": 12
                    }
                }
            },
            size=5
        )
    )
    return {similar[0]: extract_all_uuids(similar[1])}


def extract_all_uuids(response: ObjectApiResponse):
    return [hit['_source']['uuid'] for hit in response['hits']['hits']]
