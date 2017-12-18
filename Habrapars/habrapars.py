# -*- coding: utf-8 -*-

import argparse
from datetime import datetime, timedelta
import psycopg2
import parsing


# for checking datetime arguments
valid_date = lambda dt: datetime.strptime(dt, "%Y-%m-%d")

parser = argparse.ArgumentParser(description='list of title by hub')
parser.add_argument('string', type=str, nargs='*',
                    help="""'top post' - popular post from week;
                         'top hub' - top 10 popular hub in habradata;
                         'top author' - top 10 productive author;
                         <name of hub> [-a|--after YYYY-MM-DD] [-b|--before YYYY-MM-DD]
                         """)
parser.add_argument('-a', '--after',
                    type=valid_date,
                    default=datetime.today() - timedelta(days=7),
                    help='starting datetime')
parser.add_argument('-b', '--before',
                    type=valid_date,
                    default=datetime.today(),
                    help='ending datetime')
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
                    print("unknown command"
                          "\nenter '-h' for help")
        elif args.string[0] == 'update':
            try:
                if len(args.string) > 1:
                    parsing.update_base(int(args.string[1]))
            except ValueError:
                print('ERROR: second argument is not integer')
            else:
                parsing.update_base()
            print('database is updated')
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
            if len(results) == 0:
                print("nothing found at your request"
                      "\ncheck command or name of hub"
                      "\nor enter '-h' for help")
            else:
                for result in results:
                    print(*result)
