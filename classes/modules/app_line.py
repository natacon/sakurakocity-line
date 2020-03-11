# -*- coding: utf-8 -*-
import os
import random
import sys

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from . import message_util
from .app_tweepy import tweepy_api

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    messages = get_message(event.message.text)
    for m in messages:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=m))


def send_message(reply_token, message):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=message))


def get_message(text):
    if any(s in text for s in ('さく', 'こちまん', 'らこす', 'ささ', 'さぴ')):
        return [random.choice([
            'なんだ？',
            'よんだ？',
        ])]
    if any(s in text for s in ('まな', 'まき', 'ちゎ', 'ちわ')):
        return ['まきちゎ！']
    if 'お手' in text:
        return [random.choice([
            'ん？',
            'ぽむむ〜？',
            'なんだ？',
            'お手だぞ',
            'おかわりだぞ',
            '立てだぞ',
            'もっと立てだぞ'
        ])]
    if '何の日' in text:
        return [message_util.what_day(text)]
    if '記念日を教えて' in text:
        return [message_util.anniversary(text)]
    if '付き合って' in text:
        return [message_util.couple_count(text)]
    if '結婚して' in text:
        return [message_util.marriage_count(text)]
    if '何日目カウント' in text:
        return [message_util.day_count(text)]
    if 'ワートリ交換' in text:
        search_results = tweepy_api.search('(交換 OR 缶) (ワートリ OR ワールドトリガー)')
        sList = ['ついったーしらべたぞ']
        for result in search_results:
            s = str(result.id)
            s += '\n' + result.user.name
            s += '\n' + result.text
            s += '\n' + str(result.created_at)
            sList.append(s)
        return sList
