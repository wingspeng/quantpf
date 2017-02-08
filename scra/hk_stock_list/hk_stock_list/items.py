# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HkStockListItem(scrapy.Item):
    name              = scrapy.Field()       #名称
    code              = scrapy.Field()       #股票代码
    industry          = scrapy.Field()       #行业
    business          = scrapy.Field()       #主营业务
    boss              = scrapy.Field()       #老板
    trade_unit        = scrapy.Field()       #交易单位
    pass