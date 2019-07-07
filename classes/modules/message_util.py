# -*- coding: utf-8 -*-
import datetime

user_dict = {'yukinowacity': 'ゆきちゎ', 'makinowacity': 'まきちゎ'}
day_dict = {
    'couple_day': datetime.date(2015, 3, 7),
    'propose_day': datetime.date(2015, 10, 10),
    'marriage_day': datetime.date(2016, 3, 7),
    'wedding_day': datetime.date(2018, 2, 4),
}

def couple_count(message):
    diff_d = diff_day(day_dict['couple_day'], datetime.date.today())
    return '付き合って' + str(diff_d) + u'日だぞ。'

def marriage_count(message):
    diff_d = diff_day(day_dict['marriage_day'], datetime.date.today())
    print(diff_year(day_dict['marriage_day'], datetime.date.today()))
    return '結婚して' + str(diff_d) + u'日だぞ。'

# def shigoowa(message):
#     user = get_user(message)
#     message.send(user_dict[user['name']] + 'おつかれさまきゎだぞ。:こちたまん:')

def day_count(message):
    diff_couple = diff_day(day_dict['couple_day'], datetime.date.today())
    diff_marriage = diff_day(day_dict['marriage_day'], datetime.date.today())
    return '付き合って' + str(diff_couple + 1) + u'日目、結婚して' + str(diff_marriage + 1) + u'日目だぞ。'

def diff_day(d1: datetime.date, d2: datetime.date) -> int:
    if d1 > d2:
        d1, d2 = d2, d1
    return (d2 - d1).days

def diff_month(d1: datetime.date, d2: datetime.date) -> int:
    if d1 > d2:
        d1, d2 = d2, d1
    return (d2.year - d1.year) * 12 + d2.month - d1.month

def diff_year(d1: datetime.date, d2: datetime.date) -> float:
    if d1 > d2:
        d1, d2 = d2, d1
    diff_m = (d2.year - d1.year) * 12 + d2.month - d1.month
    return diff_m/12

def anniversary(message):
    return str(day_dict)

def what_day(message):
    today = datetime.date.today()
    if today.day == 7:
        if today.month == 3:
            return '付き合った日と結婚記念日だぞ'
        else:
            return '記念日だぞ'
    if today.month == 10 and today.day == 10:
        return 'プロポーズの日だぞ'
    if today.month == 2 and today.day == 4:
        return '結婚式の日だぞ'
    if today.month == 1 and today.day == 1:
        return 'まきちゎの誕生日だぞ'
    if today.month == 1 and today.day == 13:
        return 'ゆきちゎの誕生日だぞ'
    else:
        return 'ん？'
