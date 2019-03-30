# -*- coding: utf-8 -*-

import datetime
import os
import random
import sys

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# 環境変数からchannel_secret・channel_access_tokenを取得
channel_secret = os.environ['LINE_CHANNEL_SECRET']
channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if 'さく' in message:
        message = 'なんだ？'
    elif 'お手' in message:
        message = random.choice([
            'ん？',
            'ぽむむ〜？',
            'なんだ？',
            'お手だぞ',
            'おかわりだぞ',
            '立てだぞ',
            'もっと立てだぞ'
        ])
    elif '何の日' in message:
        message = what_day(message)
    elif '記念日を教えて' in message:
        message = anniversary(message)
    elif '付き合って' in message:
        message = couple_count(message)
    elif '結婚して' in message:
        message = marriage_count(message)
    elif '何日目？' in message:
        message = day_count(message)
    else:
        message = ''

    if message != '':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message))

user_dict = {'yukinowacity': 'ゆきちゎ', 'makinowacity': 'まきちゎ'}
day_dict = {
    'couple_day': datetime.date(2015, 3, 7),
    'propose_day': datetime.date(2015, 10, 10),
    'marriage_day': datetime.date(2016, 3, 7),
    'wedding_day': datetime.date(2018, 2, 4),
}


def anniversary(message):
    return str(day_dict)

def what_day(message):
    today = datetime.date.today()
    if today.month == 3 and today.day == 7:
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


if __name__ == "__main__":
    app.run()