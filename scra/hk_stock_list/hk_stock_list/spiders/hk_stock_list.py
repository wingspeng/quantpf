import scrapy
from scrapy.selector import Selector
from hk_stock_list.items import HkStockListItem

class HkListSpider(scrapy.Spider):
    name = "hk_stock_list"
    start_urls = ["http://sc.hkex.com.hk/TuniS/www.hkex.com.hk/chi/market/sec_tradinfo/stockcode/eisdeqty_c.htm"]

    def parse(self,response):
        # 从当前html中所有的table中挑选出class属性为table_grey_border的table,再在这个table下选择class属性为tr_normal的tr.
        stock_list = Selector(response=response).xpath('//table[@class="table_grey_border"]/tr[@class="tr_normal"]')
        cnt = 0
        for stock in stock_list:
            item = HkStockListItem()
            item["code"] = stock.xpath('./td/text()').extract()[0]
            item["name"] = stock.xpath('./td/a/text()').extract()[0]
            item["trade_unit"] = stock.xpath('./td/text()').extract()[1]
            href = stock.xpath('./td/a/@href').extract()[0] #在当前节点下找td节点下的a节点,获取a节点下的href属性
            request = scrapy.Request(href,callback=self.parse_stock)
            request.meta['item'] = item
            cnt = cnt + 1
            if(cnt == 100):
                break
            yield request
    def parse_stock(self,response):
        # 从当前html中挑选出colspan="3"且align="left"且height="18"且width="300"所有的td
        item = response.meta["item"]
        select_res = Selector(response=response).xpath('//td[@colspan="3" and @align="left" and @height="18" and @width="300"]/font')
        item["business"] = Selector(text=select_res.extract()[1]).xpath('//text()').extract()[0].strip()
        item["boss"] = Selector(text=select_res.extract()[2]).xpath('//text()').extract()[0].strip()
        item["industry"] = Selector(text=select_res.extract()[6]).xpath('//text()').extract()[0].strip()
        self.log('parse_stock %s' % item)
        return item