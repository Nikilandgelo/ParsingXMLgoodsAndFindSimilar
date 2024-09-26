import aiohttp
from lxml.etree import _Element, iterparse
from asyncpg import Pool
from asyncio import gather
from database import insert_into_db
from elasticsearch import AsyncElasticsearch
from elastic import indexing_to_es
import uuid
import os


async def download_xml_file(url: str):
    counter = 0
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            path: str = f'./xml_files/{response.content_disposition.filename}'
            with open(path, 'wb') as file:
                print('Downloading...\n')
                async for data in response.content.iter_chunked(1024):
                    file.write(data)
                    counter += 1
                    print(f'{(1024 * counter) / 1000000:.2f} MB downloaded')
    return path


async def process_xml_file(pool: Pool, elastic_con: AsyncElasticsearch,
                           path: str, category: str):
    tasks: list = []
    for _, object_ in iterparse(path, tag=('offer')):
        # because iterparse return nothing
        object_: _Element = object_
        old_price = float(object_.findtext(
            'oldprice', object_.findtext('price')))
        new_price = float(object_.findtext('price'))
        discount: float = old_price - new_price
        uuid_object: uuid.UUID = uuid.uuid4()

        tasks.extend(
            (insert_into_db(pool, object_, old_price,
                            new_price, discount, uuid_object),
             indexing_to_es(elastic_con, object_, uuid_object,
                            category)
            ))
        print(f'{object_.findtext("name")} added to queue')

        if len(tasks) == int(os.getenv('AMOUNT_OF_CONCURRENT_PRODUCTS')) * 2:
            print('Sending objects to databases...')
            await gather(*tasks)
            tasks.clear()
    if tasks:
        print(f'Last {len(tasks) / 2} objects sending to databases...')
        await gather(*tasks)
