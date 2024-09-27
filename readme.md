# 🌐 Project Overview
This repository contains a **Python application** designed to download, process, and store product data from XML files into `PostgreSQL` and `Elasticsearch` databases. The application leverages asynchronous programming to handle large datasets efficiently.

## 🚀 Key Features
- 📥 Asynchronous Downloads: Efficiently downloads large XML files using `aiohttp`.
- 🗄️ Data Storage: Stores product data in both `PostgreSQL` and `Elasticsearch` for structured queries and fast searching.
- 🔄 Bulk Processing: Handles bulk indexing of products to optimize performance.
- 🔍 Similarity Checks: Analyzes product similarities and retrieves relevant matches.
- 🐳 Dockerized Environment: Easily set up and run the application in a containerized environment using `Docker` and `Docker Compose`.

## 💻 Technologies Used
- **Python 3.12**: The primary language used for developing the application.
- **asyncpg**: For asynchronous PostgreSQL database interactions.
- **Elasticsearch**: A search and analytics engine for storing and querying product data.
- **aiohttp**: For making asynchronous HTTP requests to download XML files.
- **Docker**: To containerize the application and its dependencies.
- **Docker Compose**: For managing multi-container Docker applications.

## 🛠️ Setup Instructions

### 📋 Prerequisites

- `Docker` and `Docker Compose` installed on your machine.
- A `.env` file in the root directory containing the following environment variables:
  
    ```env
    POSTGRES_USER=<your_user>
    POSTGRES_PASSWORD=<your_password>
    POSTGRES_DB=<your_database>
    
    ELASTIC_PASSWORD=<your_elastic_password>
    discovery.type=single-node
    xpack.security.http.ssl.enabled=false
    
    AMOUNT_OF_CONCURRENT_PRODUCTS=25           # Adjust this value based on your needs
    ```

### 🚀 Running the Application
1. Clone the repository:

    ```bash
    git clone https://github.com/Nikilandgelo/ParsingXMLgoodsAndFindSimilar.git
    cd ParsingXMLgoodsAndFindSimilar
    ```
2. Start the services using `Docker Compose`:
   
   ```bash
    docker-compose up -d --build
    ```
    This command will build and start the `PostgreSQL`, `Elasticsearch`, and **Python application** containers.
3. Access the running services:
   - `PostgreSQL`: On port `6666`
   - `Elasticsearch`: On port `9200`, you can check it through a browser on `http://localhost:9200`

## 📜 Usage
The **Python application** accepts the following command-line arguments:
- `-u` or `--url` : Specify the URL of the XML file to download.
- `-t` or `--test` : Use a URL test XML file for processing.
- `-c` or `--check` : In the end check 7 products and their founded matches.
### 📝 Example Command
To run the application with a specific URL:
```bash
docker-compose exec python_app python main.py -u "http://example.com/products.xml"
```
To run the application with the test URL:
```bash
docker-compose exec python_app python main.py -t
```
To run the application and check founded matches from your file:
```bash
docker-compose exec python_app python main.py -c
```
## 📊 Performance Optimization Tips
> [!TIP]
>  
> Adjust the `AMOUNT_OF_CONCURRENT_PRODUCTS` in the `.env` file to control the number of products processed concurrently based on your system's capacity.
> 
> For large datasets, ensure that your `PostgreSQL` and `Elasticsearch` configurations are tuned appropriately for bulk operations. Consider increasing the CPU/memory allocation for `Docker` containers if processing slows down.
## 🛒 Product Matching Examples
Below are examples of products and their similar product matches, showcasing how the similarity search results are formatted.
```bash
Product UUID: 0001335e-fec8-40ec-b967-6c9ef502ada6
Title: Чехол на Huawei nova 10 SE / Хуавей Нова 10 SE с принтом Драконы с ножом, прозрачный
Similar Products:
 - 140fc8a7-6495-4801-acb9-cb1fca4b040a: Чехол на Huawei Nova Y72 / Хуавей Нова Y72 с принтом Драконы с ножом, прозрачный
 - 55fb7556-0409-4d29-bb34-89bf8616046c: Чехол на Huawei Nova 3 / Хуавей Нова 3 с принтом Драконы с ножом, прозрачный
 - 679a5ebe-4dfe-4ce6-afcd-407a1ff94361: Чехол на Huawei Nova Y91 / Хуавей Нова Y91 с принтом Драконы с ножом, прозрачный
 - 7a218f23-77ec-4ad5-b364-f2ccc18f3f29: Чехол на Huawei Nova 10 Pro / Хуавей Нова 10 Про с принтом Драконы с ножом, прозрачный
 - b39b232d-4abb-4b4a-8348-a3b6238b42ba: Чехол на HuaweI Nova Y61 / Хуавей Нова Y61 с принтом Драконы с ножом, прозрачный

Product UUID: 00015acc-2925-4be7-b778-4bda9eea9dfd
Title: Беспроводные наушники Live Free 2, синие
Similar Products:
 - 19ed830c-7f7c-4e75-8752-66b8af536650: Беспроводные наушники Live Free 2, розовые
 - 62fd9955-ee04-4212-888f-24f8da89f648: TWS беспроводные наушники Wireless Headset Air 16/bluetooth 5.0/быстрая зарядка/микрофон
 - 772b4f1f-94b9-4559-8f5f-07047844475d: Беспроводные наушники Hoco Apods 2
 - e1d23bb7-c438-4dd2-9843-62b9990878d9: Беспроводные наушники Live Free 2, серебристые
 - e4401c9b-5817-4aeb-826f-cf3a03d7bdd8: Беспроводные наушники Live Free 2, чёрные

Product UUID: 0001aae0-15c9-4eb0-8208-b881308025d2
Title: Ремешок для смарт-часов Realme шириной 22 мм, силиконовый, Gamma, бордовый
Similar Products:
 - 3fe4e6af-430d-49c8-9ffb-55f5ebf8260f: Ремешок для смарт-часов Realme шириной 22 мм, силиконовый, Gamma, оранжевый
 - 4b92f63b-8ea8-42c1-99e9-600eb7d61f0a: Ремешок для смарт-часов Realme шириной 22 мм, силиконовый, Gamma, черный
 - 4bd998aa-50bf-4db0-9b90-327fc87f607b: Ремешок для смарт-часов Realme шириной 22 мм, силиконовый, Gamma, желтый
 - 839423a4-8c13-48f4-b5f9-d9876dc3f17e: Ремешок для смарт-часов Realme шириной 22 мм, силиконовый, Gamma, мятный
 - b2fa3b8b-4eeb-4726-97e3-958983ae4edf: Ремешок для смарт-часов Realme шириной 22 мм, силиконовый, Gamma, красный

Product UUID: 0001cd3e-2a64-425f-aa96-4a52f179704f
Title: Силиконовый чехол COMMO Shield Case для iPhone 15 Pro, с поддержкой беспроводной зарядки, Black
Similar Products:
 - 65d7f704-3149-499e-b579-aad94be40138: Силиконовый чехол COMMO Shield Case для iPhone 15 Plus, с поддержкой беспроводной зарядки, Black
 - 92c34b1e-75e8-4127-bee6-1dc6b7d57830: Силиконовый чехол COMMO Shield Case для iPhone 15 Pro, с поддержкой беспроводной зарядки, Wine
 - 993d0526-428b-4578-a363-91aabdcaf75b: Силиконовый чехол COMMO Shield Case для iPhone 15 Pro Max, с поддержкой беспроводной зарядки, Black
 - 9c9bf373-5b8c-4be4-9b28-16fa2da21790: Силиконовый чехол COMMO Shield Case для iPhone 15 Pro, с поддержкой беспроводной зарядки, Commo Yellow
 - ee14fa09-7f78-423e-9f3e-bbeaaeb2b274: Силиконовый чехол COMMO Shield Case для iPhone 15 Pro, с поддержкой беспроводной зарядки, Commo Gray

Product UUID: 00026136-1e55-4e10-94d7-da724a741af5
Title: Чехол на Honor 9 / Хонор 9 с принтом Фон соты красные
Similar Products:
 - 0f60328c-eaed-4616-8848-ff3f7933db83: Чехол на Xiaomi Mi 9 / Сяоми Ми 9 с принтом Фон соты красные
 - 1d6a9a24-6098-4784-b1a1-9937f3581fa2: Чехол на Huawei Nova 9 SE / Хуавей Нова 9 SE с принтом Фон соты красные
 - 3671b2d7-cb9b-4541-8e24-30c4fcaffe15: Чехол на Honor 9 Lite / Хонор 9 Лайт с принтом Фон соты красные
 - 4b0bcb32-9e7e-4bda-8e0b-c733aca1d97e: Чехол на Tecno Spark 9 / Техно Спарк 9 с принтом Фон соты красные
 - cd660029-1f93-4d92-b394-582ee9743d37: Чехол на Honor 20 / Хонор 20 с принтом Фон соты красные

Product UUID: 00029c23-47d7-46a6-8ea3-b842b93cc7b4
Title: Полупрозрачный дизайнерский силиконовый чехол для Мейзу 16 Плюс / Meizu 16th Plus Кошки принт
Similar Products:
 - 06c86747-624a-46ee-86b0-a8ebeb004b3d: Полупрозрачный дизайнерский силиконовый чехол для Мейзу 16 Плюс / Meizu 16th Plus Цветочный принт
 - 27ba0b76-c66b-4a0a-83f3-61a737716280: Полупрозрачный дизайнерский силиконовый чехол для Мейзу 16 Плюс / Meizu 16th Plus Хаски
 - 6f673fd8-95f2-452d-a7b3-114e7460e0cf: Полупрозрачный дизайнерский силиконовый чехол для Мейзу 16 Плюс / Meizu 16th Plus Женские принты
 - b885f4d5-8c93-4839-937c-ab285737071d: Полупрозрачный дизайнерский силиконовый чехол для Мейзу 16 Плюс / Meizu 16th Plus Кошки
 - da8278fc-46c8-4eb6-bb17-e2a2aee1faad: Полупрозрачный дизайнерский силиконовый чехол для Мейзу 16 Плюс / Meizu 16th Plus Мама и дочь

Product UUID: 00032cfd-1795-4a47-b10b-b713c32e6f91
Title: Прозрачный силиконовый чехол с защитой камеры для телефона Huawei Honor X10 / Тонкий противоударный чехол на смартфон Хуавей Хонор Х10
Similar Products:
 - 62a46dfc-0e0e-463c-980f-cb24df067cd3: Прозрачный силиконовый чехол с защитой камеры для телефона Samsung Galaxy S23 / Тонкий противоударный чехол на смартфон Самсунг Галакси С23 
 - 69ba77d9-d55b-4f8f-aeaf-70115b343c23: Прозрачный силиконовый чехол с защитой камеры для телефона Xiaomi 12T Pro / Тонкий противоударный чехол на смартфон Сяоми 12Т Про
 - 9ec808e6-851e-4298-9620-01601b6dc42a: Прозрачный силиконовый чехол с защитой камеры для телефона Xiaomi Redmi Note 8T / Тонкий противоударный чехол на смартфон Сяоми Редми Нот 8Т
 - e02d1962-8bc2-4277-b3c9-f9d7d89358f2: Прозрачный силиконовый чехол с защитой камеры для телефона Realme C35 / Тонкий противоударный чехол на смартфон Реалми С35
 - e4cfb9db-3b9b-410b-aaf4-22b9ecc0c774: Прозрачный силиконовый чехол с защитой камеры для телефона Xiaomi 12 Lite / Тонкий противоударный чехол на смартфон Сяоми 12 Лайт

Product UUID: 00033cbb-4553-4629-bbb9-87e5129f2144
Title: Малая настольная лампа-лупа REXANT на подставке с крышкой и подсветкой 48 LED, увеличение х1.75, х7
Similar Products:
 - 0e42b02d-21ad-4855-b18b-f77f558eaf41: Лупа настольная малая 3X с подсветкой 30 LED (подставка + прищепка), белая Rexant
 - 307d0a68-ba95-4044-a767-ae8f8fd5af67: Настольная малая круглая лампа-лупа REXANT на подставке с крышкой (3+12 диоптрий) с бестеневой подсветкой
 - 3851b980-c3b4-4f51-b64c-7354681bf1f1: Косметологическая светодиодная лампа лупа LN-5 на струбцине, настольная, пятикратное увеличение, белая
 - 69544d78-f94e-4d3a-8a33-cc9b0dee5115: Настольная лампа-лупа REXANT на прищепке с крышкой с подсветкой 60 LED, увеличение х1.75, х7
 - 7b7faf0f-e1da-4266-b363-4b5bca3d8afa: Настольная круглая лампа-лупа REXANT с бестеневой подсветкой без мерцания на струбцине, увеличение х3

Product UUID: 000357c1-35c7-4b69-a3d5-148af564bada
Title: Матовый чехол Snowboarding для Samsung Galaxy S20 Ultra / Самсунг С20 Ультра с эффектом блика черный
Similar Products:
 - 357e1fab-74f3-46a1-9b21-35b4d9345342: Матовый чехол Boxing для Samsung Galaxy S20 Ultra / Самсунг С20 Ультра с эффектом блика черный
 - 7c27555e-0d4f-4e2d-88e5-05e7813fabb5: Матовый чехол Football для Samsung Galaxy S20 Ultra / Самсунг С20 Ультра с эффектом блика черный
 - 95987779-8b70-4e82-ba18-381e435a99ec: Матовый чехол Hockey для Samsung Galaxy S20 Ultra / Самсунг С20 Ультра с эффектом блика черный
 - 96ca2851-23cc-4273-b982-5a03f2a195ef: Матовый чехол Trekking для Samsung Galaxy S20 Ultra / Самсунг С20 Ультра с эффектом блика черный
 - ecd64af5-76c7-488f-8566-a61d9a4b23bf: Матовый чехол Kickboxing для Samsung Galaxy S20 Ultra / Самсунг С20 Ультра с эффектом блика черный

Product UUID: 0004498d-fcfb-4a08-91d2-58e3666d3b70
Title: Силиконовый чехол на Apple iPhone 11 Pro / Эпл Айфон 11 Про с рисунком "Кот в зеленой шапке"
Similar Products:
 - 6c01fb08-7a2d-48be-8956-ca0f51001aff: Силиконовый чехол на Apple iPhone 11 Pro Max / Эпл Айфон 11 Про Макс с рисунком "Кот в зеленой шапке"
 - 790aba03-faa1-4fde-bb21-7355fd6a7c34: Силиконовый чехол на Apple iPhone 11 Pro / Эпл Айфон 11 Про с рисунком "Недовольный кот"
 - d8f90f6d-e43e-48cf-a2d7-ea0f03de65a1: Силиконовый чехол на Apple iPhone 6s / 6 / Эпл Айфон 6 / 6с с рисунком "Кот в зеленой шапке"
 - de1fbbf9-9cab-440c-9eb3-e13f7e2bd68b: Силиконовый чехол на Apple iPhone 12 / 12 Pro / Эпл Айфон 12 / 12 Про с рисунком "Кот в зеленой шапке"
 - f81062d0-ec8b-47da-a3b9-6ca8a24723ca: Силиконовый чехол на Apple iPhone 12 Pro Max / Эпл Айфон 12 Про Макс с рисунком "Кот в зеленой шапке"

Product UUID: 0004a347-02eb-491c-a81e-6f31421ae911
Title: Чехол-книжка Река и звезды на Xiaomi Redmi 12C / Сяоми Редми 12С черный
Similar Products:
 - 766a77d9-58b0-4aaf-a9be-90254e638a25: Чехол-книжка Месяц и звезды на Xiaomi Redmi 12C / Сяоми Редми 12С черный
 - 8b6a9910-d6d4-4bbc-89a3-03625a8c311c: Чехол-книжка на Xiaomi Redmi 12C / Сяоми Редми 12С черный
 - a3a2f6d5-887a-4271-a4ab-8837e0c4345c: Чехол-книжка Река в заснеженном лесу на Xiaomi Redmi 12C / Сяоми Редми 12С золотой
 - d6a66fed-1001-4178-a4f7-26a2de40323d: Чехол-книжка Лес и звезды на Xiaomi Redmi 12C / Сяоми Редми 12С черный
 - d8dd469f-fc01-4937-9c3c-d5ec1ee258a4: Чехол-книжка Кит и облака на Xiaomi Redmi 12C / Сяоми Редми 12С черный

Product UUID: 000552c8-c5d8-4038-b605-94a5f8144e02
Title: Матовый чехол All Flowers For You для Samsung Galaxy A22 / M32 / M22 / Самсунг А22 / М32 / М22 с 3D эффектом бирюзовый
Similar Products:
 - 060218f4-f843-450d-9f15-6d756a0cc6f3: Матовый чехол The Best Of The Best для Samsung Galaxy A22 / M32 / M22 / Самсунг А22 / М32 / М22 с 3D эффектом бирюзовый
 - 31f4dd2d-3520-49d7-86c3-93c496710fa8: Матовый чехол Hands для Samsung Galaxy A22 / M32 / M22 / Самсунг А22 / М32 / М22 с 3D эффектом розовый
 - 54cf83bb-6abc-48b9-9a5f-d31680485c4f: Матовый чехол Pansies для Samsung Galaxy A22 / M32 / M22 / Самсунг А22 / М32 / М22 с 3D эффектом желтый
 - 89652206-ba4d-4561-9e35-c79068ba8162: Матовый чехол Rain для Samsung Galaxy A22 / M32 / M22 / Самсунг А22 / М32 / М22 с 3D эффектом бирюзовый
 - 9518b9c0-9b29-4729-97ac-74d245e89062: Матовый чехол Camomiles для Samsung Galaxy A22 / M32 / M22 / Самсунг А22 / М32 / М22 с 3D эффектом бирюзовый

Product UUID: 00057555-18e1-417b-9e64-ea33ae7602bb
Title: Силиконовый чехол на Samsung Galaxy M32, Самсунг М32 с принтом "Задумчивый енот"
Similar Products:
 - 03227f5d-0f2b-411e-830a-8fadec94996a: Силиконовый чехол на Samsung Galaxy M32, Самсунг М32 с принтом "Поцелуй"
 - 1a98f4f7-22ea-4721-b987-bdda7e15c6d1: Силиконовый чехол на Samsung Galaxy M32, Самсунг М32 с принтом "Климт"
 - 6381b75c-f5e6-4d99-95cf-bb9760b51bad: Силиконовый чехол на Samsung Galaxy M32, Самсунг М32 с принтом "Апельсины"
 - a6838058-f9d8-4cf9-952f-8e0867abd7d5: Силиконовый чехол на Samsung Galaxy M32, Самсунг М32 с принтом "Арбуз"
 - fa8d4b13-0911-4974-9627-9e18688156cc: Силиконовый чехол на Samsung Galaxy M32, Самсунг М32 с принтом "Леопард"

Product UUID: 0005f48f-c949-401a-9937-10fbedffca78
Title: Чехол на Realme C31 / Реалми C31 с принтом Пионы new
Similar Products:
 - 30ec8810-864e-401a-bed8-277cdb02630c: Чехол на Realme C31 / Реалми C31 с принтом Волк черно белый
 - 62815d1b-88c1-498b-947a-395de27dcd64: Чехол на Realme C31 / Реалми C31 с принтом Пыльно-розовые пионы
 - a128a9b1-32b9-4f57-975f-0af8f43da231: Чехол на Realme C31 / Реалми C31 с принтом Пионы сиреневые
 - c33e3a75-dbc7-475e-bde5-d57f5fd446e1: Чехол на Realme C31 / Реалми C31 с принтом Пионы розово-белые
 - e0113ac7-1dd7-4147-aef4-57297706f310: Чехол на Realme C31 / Реалми C31 с принтом Розовые пионы
```
## 📚 Documentation Resources
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-intro-what-is-es.html)
- [asyncpg Documentation](https://magicstack.github.io/asyncpg/current/api/index.html#)
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
