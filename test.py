# -*- coding: utf-8 -*-
import requests
from entitys.raw_data import RawData

__author__ = 'mangel'

url = "http://www.cnblogs.com/doit8791/archive/2012/05/11/2495319.html"
html = requests.get(url)
raw_data = RawData(url, str(html.content))
# print(html.content)
print(html.text)
print(len(html.content))
print(len(html.text))
RawData.test()
raw_data.save()
