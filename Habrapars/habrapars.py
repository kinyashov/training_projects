# -*- coding: utf-8 -*-

import argparse
from datetime import datetime, timedelta
import psycopg2
import utyls.updater


# for checking datetime arguments
valid_date = lambda dt: datetime.strptime(dt, "%Y-%m-%d")

parser = argparse.ArgumentParser(description='script to query to the database')

# flag for showing top of post, hub or author
parser.add_argument('-t', '--top',
                    type=str,
                    nargs='?',
                    const='post',
                    choices=['post', 'hub', 'author'],
                    help='show top post, hub or author')

# optional flag for make limit, default limit = 3
parser.add_argument('-l', '--limit',
                    type=int,
                    default=10,
                    help='how match show row in result; default=10')

# flag for update, can specify number of pages to parse
parser.add_argument('-u', '--update',
                    type=int,
                    nargs='?',
                    const=10,
                    help='update database from habrahabr to N page, e.g.: -u 10')

# optional flag for filter response by hub
parser.add_argument('-hub',
                    nargs='*',
                    type=str,
                    help='filter result by hub, register is important;'
                         'e.g: -hub Разработка веб-сайтов')

# optional flag for filter response, sets interval 7 days
parser.add_argument('-w', '--week',
                    type=valid_date,
                    nargs='?',
                    const=datetime.today() - timedelta(weeks=1),
                    help='shows result for a week')

# optional flag for filter response, sets interval from the beginning month to current day
parser.add_argument('-m', '--month',
                    type=valid_date,
                    nargs='?',
                    const=datetime(datetime.today().year, datetime.today().month, 1,
                                   hour=0, minute=0, second=0),
                    help='shows result for a current month')

# optional flag for filter response, sets beginning day
parser.add_argument('-a', '--after',
                    type=valid_date,
                    nargs='?',
                    const=datetime.today() - timedelta(weeks=1),
                    help='starting datetime; default = a week earlier; '
                         'format: YYYY-MM-DD; e.g.: -a [2017-12-11]')

# optional flag for filter response, sets ending day
parser.add_argument('-b', '--before',
                    type=valid_date,
                    default=datetime.today(),
                    help='ending datetime, default = current day, '
                         'format: YYYY-MM-DD; e.g.: -b [2017-12-18]')

args = parser.parse_args()

# sets beginning and ending days for query
# default interval = from first day current month to current day
if args.week is not None:
    left_time = args.week
    right_time = datetime.today()
elif args.month is not None:
    left_time = args.month
    right_time = datetime.today()
elif args.after is not None or args.before is not None:
    left_time = args.after
    right_time = args.before
    if left_time is None:
        left_time = datetime(datetime.today().year, datetime.today().month, 1,
                             hour=0, minute=0, second=0)

with psycopg2.connect("dbname=habradata") as conn:
    with conn.cursor() as cur:
        if args.top == 'author':
            cur.execute("""
                        SELECT author, 
                        COUNT(author) as c
                        FROM habrapost
                        WHERE time BETWEEN %s AND %s 
                        GROUP BY author 
                        ORDER BY c DESC
                        LIMIT %s
                        """,
                        (left_time, right_time, args.limit))
            results = cur.fetchall()
            for result in results:
                print(*result)
        elif args.top == 'hub':
            cur.execute("""
                        SELECT hub, 
                        COUNT(hub) as c
                        FROM habrahub
                        WHERE id IN  
                            (SELECT id 
                            FROM habrapost
                            WHERE time BETWEEN %s AND %s)
                        GROUP BY hub
                        ORDER BY c DESC
                        LIMIT %s
                        """,
                        (left_time, right_time, args.limit))
            results = cur.fetchall()
            for result in results:
                print(*result)
        elif args.top == 'post':
            cur.execute("""
                        SELECT title
                        FROM habrapost
                        WHERE time BETWEEN %s AND %s
                        LIMIT %s
                        """,
                        (left_time, right_time, args.limit))
            results = cur.fetchall()
            for result in results:
                print(*result)

        if args.update is not None:
            utyls.updater.update_base(args.update)
            print('database is updated')

        if args.hub is not None:
            cur.execute("""
                        SELECT title
                        FROM habrapost
                        WHERE time BETWEEN %s AND %s
                        AND id IN  
                            (SELECT id 
                            FROM habrahub 
                            WHERE hub = %s)
                        LIMIT %s
                        """,
                        (left_time, right_time, ' '.join(args.hub), args.limit))
            results = cur.fetchall()
            if len(results) == 0:
                print("nothing found at your request"
                      "\ncheck command or name of hub"
                      "\nor enter '-h' for help")
            else:
                for result in results:
                    print(*result)
