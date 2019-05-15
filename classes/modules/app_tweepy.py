# -*- coding: utf-8 -*-
import os

import tweepy

consumer_api_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_api_secret_key = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
auth.set_access_token(access_token, access_token_secret)

tweepy_api = tweepy.API(auth)
