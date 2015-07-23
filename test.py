# -*- coding: utf-8 -*-

import requests
from entitys.raw_data import RawData
from spider.utils import Util

__author__ = 'mangel'

url = "http://www.cnblogs.com/doit8791/archive/2012/05/11/2495319.html"
html = requests.get(url)
raw_data = RawData(url, html.text)
# print(html.content)
# print(html.text)
# print(len(html.content))
# print(len(html.text))
# print(html.encoding)
results = RawData.get_all()
for result in results:
    print result
# raw_data.save(Util.get_spider_conn())
