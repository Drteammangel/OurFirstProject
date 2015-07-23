# -*- coding: utf-8 -*-

import mysql.connector

__author__ = 'mangel'


class RawData(object):
    def __init__(self, url, data):
        self.__url = url
        self.__data = data

    @staticmethod
    def test():
        conn = mysql.connector.connect(user='root', password='', database='spider')
        cursor = conn.cursor()
        cursor.execute("select * from raw_data;")
        values = cursor.fetchall()
        conn.commit()
        cursor.close()
        print(values)

    def save(self):
        conn = mysql.connector.connect(user='root', password='', database='spider')
        cursor = conn.cursor()
        cursor.execute("insert into raw_data (url, data) VALUES (%s, %s)", [self.__url, self.__data])
        print(cursor.rowcount)
        conn.commit()
        cursor.close()
