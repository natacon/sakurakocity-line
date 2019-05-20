# -*- coding: utf-8 -*-
import sys

from flask import Flask, request, abort

from classes.modules import app_line

app = Flask(__name__)


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
        app_line.handler.handle(body, signature)
    except:
        print(sys.exc_info())
        abort(400)

    return 'OK'


if __name__ == "__main__":
    app.run()
