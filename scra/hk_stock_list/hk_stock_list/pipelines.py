# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import class_pymysql
from scrapy import log
class HkStockListPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mysql_ = MYSQL("localhost","root","123456","stock")

    def process_item(self, item, spider):
        log.msg('process_item %s' % item)
        sql = """INSERT INTO hk_basic(NAME,CODE,industry,business,boss,trade_unit)
                VALUES ('%%s','%%s','%%s','%%s','%%s','%%s')"""
                % (item["name"],item["code"],item["industry"],item["business"],item["boss"],item["trade_unit"])

        mysql_.ExecNonQuery(sql)
        return item
