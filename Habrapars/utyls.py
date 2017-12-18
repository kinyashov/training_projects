# -*- coding: utf-8 -*-

from datetime import datetime


def habratime_isotime(date):

    """Highly specialized function for converts date such 'N месяц HH:MM'
    which used in habrahabra site.

    :param date: takes only 'день месяца|сегодня|вчера HH:MM' format
    :return: datetime format for SQL and Python
    """

    # array for comparison and to find need a month
    month_names = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

    # function always takes current year for user
    year = datetime.today().year

    dt = date.lstrip().split(' ')

    # if date have some string instead 'day of month'
    # function takes current day and current month for current user
    if dt[0] == 'сегодня':
        day = datetime.today().day
        month = datetime.today().month
        # hours and minutes is always in the end
        hm = dt[-1]
    elif dt[0] == 'вчера':
        day = datetime.today().day - 1
        # if 'yesterday' is in another month
        if day > datetime.today().day:
            month = datetime.today().month - 1
        else:
            month = datetime.today().month
        hm = dt[-1]
    else:
        # for usual format
        day, month, _, hm = dt
        month = month_names.index(month[0:3]) + 1

    hour, minute = hm.split(':')

    day, hour, minute = map(lambda x: int(x), [day, hour, minute])

    t = datetime(year, month, day, hour=hour, minute=minute, second=0)
    return t
