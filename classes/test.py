# -*- coding: utf-8 -*-
from classes.modules import app_line

messages = app_line.get_message('ワートリ交換')
print(messages)
for m in messages:
    print(m)
