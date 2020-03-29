# -*- coding: utf-8 -*-
import pymysql
class Database:
    def __init__(self,user_name,passwd,host_name,db_name):
        try:

            self.connection = pymysql.connect(host=host_name,
                                 user=user_name,
                                 password=passwd,
                                 db=db_name,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)





