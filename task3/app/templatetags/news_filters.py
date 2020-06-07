from datetime import datetime, timedelta
from pprint import pprint

from django import template


register = template.Library()


@register.filter
def format_date(value):
    a = [2,3,4,22,24]
    ov = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    value = datetime.fromtimestamp(int(value))
    if datetime.now() - value < timedelta(minutes= 10):
        return ('Только что')
    elif datetime.now() - value < timedelta(hours= 24):
        dtime = datetime.now() - value
        dtime = round(dtime.seconds/3600)
        if dtime in a:
            return (f'{dtime} часа назад')
        elif dtime in ov:
            return (f'{dtime} часов назад')
        else:
            return (f'{dtime} час назад')
    elif datetime.now() - value > timedelta(hours=24):
        return value


@register.filter
def format_score(value = 'Отсутсвует'):
    if value < -5:
        return ('все плохо')
    elif value >=-5 and value < 5:
        return ('нейтрально')
    elif value >= 5:
        return ('хорошо')


@register.filter
def format_num_comments(value):
    if value == 0:
        return ('Оставьте комментарий')
    elif value >0 and value <=50:
        return value
    elif value >= 50:
        return ('50+ комментариев')

@register.filter
def format_selftext(value, count):
    list_value = value.split(' ')
    if len(list_value) > count * 2:
        return (f"{' '.join(list_value[:count])} ... {' '.join(list_value[len(list_value)-5:])}")
    else:
        return (value)




