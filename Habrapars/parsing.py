import urllib3
from html.parser import HTMLParser
import timeformat
import psycopg2

is_author = False
is_id = False
is_date = False
is_hub = False
is_title = False
dict_title_table = {}
dict_hub_table = {}


def update_base():
    with psycopg2.connect("dbname=habradata") as conn:
        with conn.cursor() as cur:
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS habrapost (
                        id text PRIMARY KEY,
                        author text NOT NULL,
                        time timestamp NOT NULL,
                        title text NOT NULL
                        );
                        """)
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS habrahub (
                        index serial PRIMARY KEY,
                        id text NOT NULL,
                        hub text NOT NULL
                        );
                        """)

            class MyHTMLParser(HTMLParser):

                def handle_starttag(self, tag, attrs):
                    global is_id
                    global is_author
                    global is_date
                    global is_title
                    global is_hub
                    if ('class', 'inline-list__item-link hub-link ') in attrs:
                        is_hub = True
                    for attr in attrs:
                        if is_id is True:
                            if attr[0] == 'id':
                                dict_title_table.update([attr])
                                dict_hub_table.update([attr])
                            is_id = False
                        if attr == ('class', 'user-info__nickname user-info__nickname_small'):
                            is_author = True
                        if attr == ('class', 'content-list__item content-list__item_post shortcuts_item'):
                            is_id = True
                        if attr == ('class', 'post__time'):
                            is_date = True
                        if attr == ('class', 'post__title_link'):
                            is_title = True

                def handle_data(self, data):
                    global is_author
                    global is_date
                    global is_title
                    global dict_title_table
                    global is_hub
                    global dict_hub_table
                    if is_author is True:
                        dict_title_table['author'] = data
                        is_author = False
                    if is_date is True:
                        data = timeformat.habratime_isotime(data)
                        dict_title_table['date'] = data
                        is_date = False
                    if is_title is True:
                        dict_title_table['title'] = data
                        is_title = False
                        cur.execute("""
                                    INSERT INTO habrapost (id, author, time, title) 
                                    VALUES (%s, %s, %s, %s)
                                    ON CONFLICT (id) DO NOTHING;
                                    """,
                                    (dict_title_table['id'],
                                     dict_title_table['author'],
                                     dict_title_table['date'],
                                     dict_title_table['title'])
                                    )
                        conn.commit()
                    if is_hub is True:
                        dict_hub_table['hub'] = data
                        is_hub = False
                        cur.execute("""
                                    INSERT INTO habrahub (hub, id) 
                                    VALUES (%s, %s);
                                    """,
                                    (dict_hub_table['hub'],
                                     dict_hub_table['id'])
                                    )
                        conn.commit()

            http = urllib3.PoolManager()
            for i in range(1, 12):
                r = http.request('GET', 'https://habrahabr.ru/top/monthly/page{}/'.format(i))
                res = r.data.decode('utf-8')
                parser = MyHTMLParser()
                parser.feed(res)
