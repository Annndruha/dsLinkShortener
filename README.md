# Link shortener
Простое приложение на Python, которое позволяет сокращать ссылки на своём домене. 

## Использование
Для работы сервиса требуется база данных и СУБД PostgreSQL. Конфигурационный файл базы данных сравниться в папке `config/database.json` и имеет следующий формат:

    {
        'host': 'localhost',
        'port': '5432', 
        'user': 'root', 
        'password': '', 
        'dbname': 'postgres', 
        'scheme': 'public'
    }

В схеме базы данных, в которой будет работать ваш сокращатель ссылок, необходимо предварительно создать таблицы users и links:

    CREATE TABLE linkshortener.users (
        id oid NOT NULL,
        login varchar NOT NULL,
        access_code varchar(24) NOT NULL,
        isdeleted bool NOT NULL DEFAULT false,
        CONSTRAINT users_pk PRIMARY KEY (id)
    );
    
    CREATE TABLE linkshortener.links (
        id oid NOT NULL,
        link varchar NOT NULL,
        alias varchar NOT NULL,
        creator oid NOT NULL DEFAULT 0,
        visits int4 NOT NULL DEFAULT 0,
        isdeleted bool NOT NULL DEFAULT false,
        CONSTRAINT links_pk PRIMARY KEY (id),
        CONSTRAINT links_fk FOREIGN KEY (creator) REFERENCES linkshortener.users(id)
    );  
    INSERT INTO linkshortener.links (id, link, alias, creator, visits, isdeleted) 
    VALUES(0, 'localhost', 'N/A', 0, 0, false);

В таблице users создайте необходимое количество пользователей. Ключ access_code рекомендуется генерировать случайным образом, т.к. он является единственным средством защиты от несанкционированного доступа. 

    INSERT INTO linkshortener.users (id, login, access_code, isdeleted) 
    VALUES(0, 'admin', 'AeyOS4VqwxG2v4IQpv2FKJGy');

Для создания ссылок перейдите на страницу `http://example.com/make/<access_code>` и введите ссылку которую нужно сократить (текст сокращённой ссылки по желанию), или сделайте POST запрос на этот адрес с параметрами `link` – ссылка, которая должна быть сокращена, и `alias` – сокращённое имя вашей ссылки (оба параметра обязательны).

Самый простой способ запустить сервис - ввести в консоли:

    git clone https://github.com/dyakovri/dsLinkShortener
    pip install -r dsLinkShortener/requirements.txt
    python dsLinkShortener/__main__.py
    
Можно с помощью Docker:

    docker build https://github.com/dyakovri/dsLinkShortener -t linkshortener:latest
    docker run -d -p 80 -v <path>/<to>/config/database.json:/home/LinkShortener/config/database.json --name linkshortener linkshortener
    
Это запустит сокращатель ссылок на порту 80.
