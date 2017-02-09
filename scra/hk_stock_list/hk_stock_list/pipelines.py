# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import pymysql
sys.path.append('../../common/')
import class_pymysql
from scrapy import log
class HkStockListPipeline(object):
    def __init__(self):
        self.mysql_ = class_pymysql.MYSQL("localhost","root","123456","stock")

    def process_item(self, item, spider):
        log.msg('process_item %s' % item)
        name = pymysql.escape_string(item["name"])
        code = pymysql.escape_string(item["code"])
        industry = pymysql.escape_string(item["industry"])
        business = pymysql.escape_string(item["business"])
        boss = pymysql.escape_string(item["boss"])
        trade_unit = pymysql.escape_string(item["trade_unit"])
        sql = """INSERT INTO hk_basic(name,code,industry,business,boss,trade_unit)
                VALUES ('%s','%s','%s','%s','%s','%s')""" % (name,code,industry,business,boss,trade_unit)
        log.msg('sql : %s' % sql)
        self.mysql_.ExecNonQuery(sql)
        return item
