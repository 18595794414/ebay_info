# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class EbayItemShop(scrapy.Item):
    seller_name = scrapy.Field()
    followers_num = scrapy.Field()
    country = scrapy.Field()
    positive_feedback_percer = scrapy.Field()
    Feedback_score = scrapy.Field()
    Item_s_described_score = scrapy.Field()
    Communication_score = scrapy.Field()
    Shipping_time_score = scrapy.Field()
    Shipping_charges_score = scrapy.Field()
    seller_text = scrapy.Field()
    Positive_feedback = scrapy.Field()
    Neutral_feedback = scrapy.Field()
    Negative_feedback = scrapy.Field()
    views = scrapy.Field()
    Reviews = scrapy.Field()
    goods_num = scrapy.Field()
    Member_since = scrapy.Field()
    shop_url = scrapy.Field()
    html = scrapy.Field()


class EbayItemGood(scrapy.Item):
    good_id = scrapy.Field()
    good_name = scrapy.Field()
    price_dollar = scrapy.Field()
    price_RMB = scrapy.Field()
    project_location = scrapy.Field()
    brand = scrapy.Field()
    seller_name = scrapy.Field()
    sales_count = scrapy.Field()
    cat_1 = scrapy.Field()
    cat_2 = scrapy.Field()
    cat_3 = scrapy.Field()
    cat_4 = scrapy.Field()
    cat_5 = scrapy.Field()
    cat_6 = scrapy.Field()
    html = scrapy.Field()
