import asyncpg
from asyncpg import Pool, connect
import os
import json
from lxml.etree import _Element
from collections import defaultdict


async def get_db_connection() -> Pool:
    return await asyncpg.create_pool(
        password=os.getenv("POSTGRES_PASSWORD"),
        user=os.getenv("POSTGRES_USER"),
        database=os.getenv("POSTGRES_DB"),
        host='postgres',
        port=5432,
        max_size=int(os.getenv('AMOUNT_OF_CONCURRENT_PRODUCTS'))
    )


async def insert_into_db(pool: Pool, offer: _Element, old_price: float,
                         new_price: float, discount: float, uuid_object):
    async with pool.acquire() as connection:
        await connection.execute(
            '''
            INSERT INTO sku
            (uuid, marketplace_id, product_id, title, description,
            brand, seller_id, seller_name, first_image_url,
            category_id, category_lvl_1, category_lvl_2,
            category_lvl_3, category_remaining, features,
            rating_count, rating_value, price_before_discounts,
            discount, price_after_discounts, bonuses, sales, currency,
            barcode)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10,
            $11, $12, $13, $14, $15, $16, $17, $18, $19, $20,
            $21, $22, $23, $24)
            ''',
            uuid_object,
            1,
            int(offer.attrib.get('id')),
            offer.findtext('name'), 
            offer.findtext('description'),
            offer.findtext('vendor'),
            int(offer.findtext('group_id')),
            offer.findtext('vendor'),
            offer.findtext('picture'),
            int(offer.findtext('categoryId')),
            '', '', '', '',
            json.dumps(
                {param.attrib.get('name'): param.text
                for param in offer.iterfind('param')},
                ensure_ascii = False
            ),
            0,
            0.0,
            old_price,
            discount,
            new_price,
            0,
            0,
            offer.findtext('currencyId'),
            offer.findtext('barcode', '')
        )


async def add_similar_products(pool: Pool, *args: tuple[dict[str, list]]):
    async with pool.acquire() as connection:
        data = [
            (uuid, similar_uuids) 
            for arg in args 
            for uuid, similar_uuids in arg.items()
        ]
        await connection.executemany(
            '''
            UPDATE sku
            SET similar_sku = $2
            WHERE uuid = $1
            ''', data)


async def get_result_of_work():
    connection = await connect(
        password=os.getenv("POSTGRES_PASSWORD"),
        user=os.getenv("POSTGRES_USER"),
        database=os.getenv("POSTGRES_DB"),
        host='postgres',
        port=5432)
    results: list = await connection.fetch(
        '''
        SELECT
        s.uuid, s.title, s.similar_sku,
        s2.uuid AS similar_uuid, s2.title AS similar_title
        FROM sku s
        JOIN sku s2 ON s2.uuid = ANY(s.similar_sku)
        ORDER BY s.uuid
        LIMIT 70
        '''
    )
    product_dict = defaultdict(list)
    for record in results:
        product_dict[(record['uuid'], record['title'])].append({
            'similar_uuid': record['similar_uuid'],
            'similar_title': record['similar_title']
        })
    for (product_uuid, product_title), similar_items in product_dict.items():
        print((f"\nProduct UUID: {product_uuid}\nTitle: {product_title}"
              "\nSimilar Products:"))
        for similar in similar_items:
            print(f" - {similar['similar_uuid']}: {similar['similar_title']}")
