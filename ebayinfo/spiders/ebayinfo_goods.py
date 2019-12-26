# -*- coding: utf-8 -*-
import re

import scrapy

from scrapy_redis.spiders import RedisSpider
from ebayinfo.items import EbayItemGood


class EbayinfoShopSpider(RedisSpider):
    name = 'ebayinfo_goods'
    allowed_domains = ['ebay.com']
    redis_key = 'ebayinfo_goods:start_urls'


    # 使用单独的redis配置
    custom_settings = {
        'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
        'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
        'REDIS_URL': 'redis://192.168.0.230:6379/10',
        'SCHEDULER_PERSIST': True,
    }

    # 构造商品列表页url
    def parse(self, response):
        with open(r'W:/Gc/ebayinfo/1.txt', 'r', encoding='utf-8') as f:
            sellers_name = f.readlines()
            for seller_name in sellers_name:
                seller = seller_name.strip()

                goods_list = f'https://www.ebay.com/sch/{seller}/m.html?_nkw&_armrs=1&_from&rt=nc&LH_PrefLoc=6'
                yield scrapy.Request(url=goods_list,
                                     callback=self.parse_list,
                                     )

    # 获取商品url，和下一页url
    def parse_list(self, response):


        if response.xpath('//ul[@id="ListViewInner"]'):

            # # 保存列表页源码
            # with open(r'D:/Spider_Demo/goods_list_html/' + seller_name + str(self.count) + '.html', 'w', encoding='utf-8') as f:
            #     f.write(response.text)

            goods_urls = response.xpath('//ul[@id="ListViewInner"]/li/h3/a/@href').getall()

            for url in goods_urls:
                yield scrapy.Request(url=url,
                                     callback=self.parse_goodinfo)


            if response.xpath('//td[@class="pagn-next"]'):
                next_page = response.xpath('//td[@class="pagn-next"]/a/@href').get()
                if next_page != 'javascript:;':

                    yield scrapy.Request(url=next_page,
                                         callback=self.parse_list)


    # 获取商品详情
    def parse_goodinfo(self, response):

        good_id = re.search(r'itm.+/(\d+)', response.url)

        if good_id != None:
            good_id = good_id.group(1)
        html = response.body.decode()
        good_name = response.xpath('//h1[@id="itemTitle"]/text()').get()
        price_dollar = response.xpath('//span[@id="prcIsum"]/@content').get()
        price_RMB = response.xpath('//div[@id="prcIsumConv"]/span/text()').get()
        if price_RMB != None:
            price_RMB = price_RMB.split()[1]
        project_location = response.xpath('//span[@itemprop="availableAtOrFrom"]/text()').get()
        brand = response.xpath('//span[@itemprop="name"]/text()').getall()
        if brand != []:
            brand = brand[-1]
        else:
            brand = ''
        seller_name = response.xpath('//span[@class="mbg-nw"]/font/font/text()|//span[@class="mbg-nw"]/text()').get()
        sales_count = response.xpath('//a[@class="vi-txt-underline"]/text()').get()
        if sales_count != None:
            sales_count = sales_count.split()[0]
        else:
            sales_count = ''
        cats = response.xpath('//li[@class="bc-w"]//span/text()').getall()
        if len(cats) == 0:
            cat_1 = cat_2 = cat_3 = cat_4 = cat_5 = cat_6 = ''
        elif len(cats) == 1:
            cat_1 = cats[0]
            cat_2 = cat_3 = cat_4 = cat_5 = cat_6 = ''
        elif len(cats) == 2:
            cat_1, cat_2 = cats[0], cats[1]
            cat_3 = cat_4 = cat_5 = cat_6 = ''
        elif len(cats) == 3:
            cat_1, cat_2, cat_3 = cats[0], cats[1], cats[2]
            cat_4 = cat_5 = cat_6 = ''
        elif len(cats) == 4:
            cat_1, cat_2, cat_3, cat_4 = cats[0], cats[1], cats[2], cats[3]
            cat_5 = cat_6 = ''
        elif len(cats) == 5:
            cat_1, cat_2, cat_3, cat_4, cat_5 = cats[0], cats[1], cats[2], cats[3], cats[4]
            cat_6 = ''
        else:
            cat_1, cat_2, cat_3, cat_4, cat_5, cat_6, = cats[0], cats[1], cats[2], cats[3], cats[4], cats[5]

        item = EbayItemGood(good_id=good_id, good_name=good_name, price_dollar=price_dollar, price_RMB=price_RMB,
                            project_location=project_location, brand=brand, seller_name=seller_name,
                            sales_count=sales_count, cat_1=cat_1, cat_2=cat_2, cat_3=cat_3, cat_4=cat_4, cat_5=cat_5,
                            cat_6=cat_6, html=html)
        yield item