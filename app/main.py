from argparse import ArgumentParser, Namespace
import asyncio
from dotenv import load_dotenv
from xml import download_xml_file, process_xml_file
from database import get_db_connection, get_result_of_work
from elastic import get_es_connection, get_chunk_of_products


async def main(url: str, check: bool, test: bool):
    if check:
        await get_result_of_work()
        return
    if test and not url:
        url = ("http://export.admitad.com/ru/webmaster/websites/777011/"
               "products/export_adv_products/?user=bloggers_style&"
               "code=uzztv9z1ss&feed_id=21908&format=xml")
    if not url:
        raise RuntimeError((
            "\n\nNo URL provided, use -u or --url with your URL "
            "or pass -t or --test to try with the test XML file.\n"))
    pool, elastic_con, path_to_file = await asyncio.gather(
        get_db_connection(),
        get_es_connection(),
        download_xml_file(url))
    category = 'products'
    await process_xml_file(pool, elastic_con, path_to_file, category)
    await get_chunk_of_products(elastic_con, category, pool)
    await elastic_con.close()


if __name__ == '__main__':
    parser = ArgumentParser(
        description="Download and process an XML file from a URL.")
    parser.add_argument('-u', '--url',
                        help="The URL of the XML file to download.")
    parser.add_argument('-c', '--check', action="store_true",
                        help="Check finding matches.")
    parser.add_argument('-t', '--test', action="store_true",
                        help="Test XML file of products.")
    args: Namespace = parser.parse_args()
    load_dotenv(override=True)
    asyncio.run(main(args.url, args.check, args.test))
