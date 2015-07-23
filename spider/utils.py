# -*- coding: utf-8 -*-

import ConfigParser
import mysql.connector

__author__ = 'mangel'

config_path = "resources/db_config.ini"


class Util(object):
    @staticmethod
    def get_spider_conn():
        cf = ConfigParser.ConfigParser()
        cf.read(config_path)
        db_host = cf.get("spider", "host")
        db_port = cf.getint("spider", "port")
        db_user = cf.get("spider", "user")
        db_pwd = cf.get("spider", "password")
        db_name = cf.get("spider", "db_name")
        return mysql.connector.connect(user=db_user, port=db_port, host=db_host, password=db_pwd, database=db_name)
