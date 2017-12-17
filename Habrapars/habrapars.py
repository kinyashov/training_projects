import argparse
from datetime import datetime
import psycopg2
import parsing


valid_date = lambda dt: datetime.strptime(dt, "%Y-%m-%d")

parser = argparse.ArgumentParser(description='list of title by hub')
parser.add_argument('string', type=str, nargs='*')
parser.add_argument('-a', '--after', type=valid_date, default='2017-11-11')
parser.add_argument('-b', '--before', type=valid_date, default=datetime.today())

args = parser.parse_args()

with psycopg2.connect("dbname=habradata") as conn:
    with conn.cursor() as cur:
        if args.string[0] == 'top':
            if len(args.string) > 1:
                if args.string[1] == 'author':
                    cur.execute("""
                            SELECT author, 
                            COUNT(author) as c
                            FROM habrapost
                            GROUP BY author 
                            ORDER BY c DESC
                            LIMIT 10
                            """)
                    results = cur.fetchall()
                    for result in results:
                        print(*result)
                elif args.string[1] == 'hub':
                    cur.execute("""
                            SELECT hub, 
                            COUNT(hub) as c
                            FROM habrahub
                            GROUP BY hub
                            ORDER BY c DESC
                            LIMIT 10
                            """)
                    results = cur.fetchall()
                    for result in results:
                        print(*result)
                elif args.string[1] == 'post':
                    cur.execute("""
                            SELECT title
                            FROM habrapost
                            WHERE time BETWEEN CURRENT_DATE - integer '7'
                            AND CURRENT_DATE
                            """)
                    results = cur.fetchall()
                    for result in results:
                        print(*result)
                else:
                    print('я вас не понял')
        elif args.string[0] == 'update':
            parsing.update_base()
        elif type(args.string[0]) is str:
            cur.execute("""
                    SELECT title
                    FROM habrapost
                    WHERE time BETWEEN %s AND %s
                    AND id IN  
                        (SELECT id 
                        FROM habrahub 
                        WHERE hub = %s)
                    """,
                        (args.after,
                         args.before,
                         args.string[0]))
            results = cur.fetchall()
            for result in results:
                print(*result)
