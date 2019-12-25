# -*- coding: utf-8 -*-
import re


import scrapy
from scrapy_redis.spiders import RedisSpider

from ebayinfo.items import EbayItemShop


class EbayinfoShopSpider(RedisSpider):
    name = 'ebayinfo_shop'
    allowed_domains = ['ebay.com']
    redis_key = 'ebayinfo_shop:start_urls'

    # 使用单独的redis配置
    custom_settings = {
        'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
        'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
        'REDIS_URL': 'redis://192.168.0.230:6379/9',
        'SCHEDULER_PERSIST': True,
    }

    # 构造商店详情url
    def parse(self, response):
        with open(r'W:/Gc/ebayinfo/1.txt', 'r', encoding='utf-8') as f:
            sellers_name = f.readlines()
            for seller_name in sellers_name:
                seller = seller_name.strip()
                shop_url = f'https://www.ebay.com/usr/{seller}'
                yield scrapy.Request(url=shop_url,
                                     callback=self.parse_shop,
                                     meta={'seller': seller})

    # 获取商家详情
    def parse_shop(self, response):
        global Shipping_time_score, Item_s_described_score, Communication_score, Shipping_charges_score, Positive_feedback, Neutral_feedback, Negative_feedback

        if response.status == 200:
            seller = response.meta['seller']
            seller_name = re.sub(r'\*|\.|\。|\\|\?|\:|\\"|\||"|\<|\》|/', '', seller)

            # 保存商店源码
            with open(r'D:/Spider_Demo/shop_html/' + seller_name + '.html', 'a', encoding='utf-8') as f:
                f.write(response.text)

            followers_num = response.xpath('//div[@class="mem_info"]/span[1]/span/span/text()').get()
            if followers_num != None:
                followers_num = ''
            country = response.xpath('//div[@class="mem_info"]/span[last()]/text()').get()
            positive_feedback_percer = response.xpath('//div[@class="perctg"]/text()').get()
            if positive_feedback_percer:
                positive_feedback_percer = positive_feedback_percer.split()[0]
            Feedback_score = response.xpath('//span[@class="mbg-l"]/a[last()]/text()').get()
            seller_text = response.xpath('//h2[@class="bio inline_value"]/text()').get()
            if seller_text != None:
                seller_text = ' '.join(seller_text.split())
            feedback = response.xpath('//div[@class="score"]/span[@class="num"]/text()').getall()
            if feedback != []:
                Positive_feedback = feedback[0]
                Neutral_feedback = feedback[1]
                Negative_feedback = feedback[2]
            else:
                Positive_feedback = ''
                Neutral_feedback = ''
                Negative_feedback = ''
            views = re.search(r'class="info" &gt;(.*?)&lt;/span&gt; Views', response.text)
            if views:
                views = views.group(1)
            Reviews = response.xpath('//div[@class="mem_info"]/span[3]/span/span/text()').get()
            if Reviews != None:
                Reviews = ''
            goods_num = response.xpath('//span[@class="sell_count"]/a/text()').get()
            Member_since = response.xpath('//div[@class="mem_info"]/span[5]/span[2]/text()').get()
            shop_url = response.xpath('//span[@class="sell_count"]/a/@href').get()
            scores = response.xpath('//div[@class="fl each"]/span[starts-with(@class, "dsr_count")]/text()').getall()
            if scores != []:
                Item_s_described_score = scores[0]
                Communication_score = scores[1]
                Shipping_time_score = scores[2]
                Shipping_charges_score = scores[3]
            else:
                Item_s_described_score = ''
                Communication_score = ''
                Shipping_time_score = ''
                Shipping_charges_score = ''

            item = EbayItemShop(seller_name=seller_name, followers_num=followers_num, country=country,
                                positive_feedback_percer=positive_feedback_percer, Feedback_score=Feedback_score,
                                Item_s_described_score=Item_s_described_score, Communication_score=Communication_score,
                                Shipping_time_score=Shipping_time_score, Shipping_charges_score=Shipping_charges_score,
                                seller_text=seller_text, Positive_feedback=Positive_feedback,
                                Neutral_feedback=Neutral_feedback, Negative_feedback=Negative_feedback, views=views,
                                Reviews=Reviews, goods_num=goods_num, Member_since=Member_since, shop_url=shop_url)

            yield item