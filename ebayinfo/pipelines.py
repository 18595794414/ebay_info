# -*- coding: utf-8 -*-

from .items import EbayItemGood
from .items import EbayItemShop



class SavePipeline(object):
    item1 = []
    item2 = []

    def process_item(self, item, spider):

        # 商店详情信息
        if isinstance(item, EbayItemShop):

            data = (item['seller_name'], item['followers_num'], item['country'], item['positive_feedback_percer'],item['Feedback_score'], item['Item_s_described_score'], item['Communication_score'],item['Shipping_time_score'], item['Shipping_charges_score'], item['seller_text'],item['Positive_feedback'], item['Neutral_feedback'], item['Negative_feedback'], item['views'],item['Reviews'], item['goods_num'], item['Member_since'], item['shop_url'])

            self.item1.append(data)

            if len(self.item1) == 10:
                for i in self.item1:
                    with open(r'D:/Spider_Demo/ebay/shopinfo.txt', 'a', encoding='utf-8') as f:
                        f.write(str(i) + ',' + '\n')
                self.item1 = []

        # 商品详情信息
        elif isinstance(item, EbayItemGood):

            data = (item['good_id'], item['good_name'], item['price_dollar'], item['price_RMB'], item['project_location'],item['brand'], item['seller_name'], item['sales_count'], item['cat_1'], item['cat_2'], item['cat_3'], item['cat_4'],item['cat_5'], item['cat_6'])

            self.item2.append(data)

            if len(self.item2) == 20:
                for i in self.item2:
                    with open(r'D:/Spider_Demo/ebay/goodsinfo.txt', 'a', encoding='utf-8') as f:
                        f.write(str(i) + ',' +'\n')
                self.item2 = []

        return item




# class EbayPipeline(object):
#     count1 = 0
#     count2 = 0
#     item1 = []
#     item2 = []
#
# def process_item(self, item, spider):
#
#         if isinstance(item, EbayItemShop):
#
#             # 商店表连接
#             conn1 = pymysql.Connect(host='49.235.104.232', port=3306, user='root', passwd='root', db='shop',
#                                          charset='utf8')
#             cursor1 = conn1.cursor()
#
#             data = (item['seller_name'], item['followers_num'], item['country'], item['positive_feedback_percer'],
#                     item['Feedback_score'], item['Item_s_described_score'], item['Communication_score'],
#                     item['Shipping_time_score'], item['Shipping_charges_score'], item['seller_text'],
#                     item['Positive_feedback'], item['Neutral_feedback'], item['Negative_feedback'], item['views'],
#                     item['Reviews'], item['goods_num'], item['Member_since'], item['shop_url'])
#
#             self.item1.append(data)
#
#             if len(self.item1) == 10:
#
#                 print('------------开始插入商店数据-------------')
#                 sql = '''
#                     insert into shopinfo
#                     values
#                     (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                     on duplicate key update
#                     seller_name = values(seller_name), followers_num = values(followers_num), country = values(country), positive_feedback_percer = values(positive_feedback_percer), Feedback_score = values(Feedback_score), Item_s_described_score = values(Item_s_described_score), Communication_score = values(Communication_score), Shipping_time_score = values(Shipping_time_score), Shipping_charges_score = values(Shipping_charges_score), seller_text = values(seller_text), Positive_feedback = values(Positive_feedback), Neutral_feedback = values(Neutral_feedback), Negative_feedback = values(Negative_feedback), views = values(views), Reviews = values(Reviews), goods_num = values(goods_num), Member_since = values(Member_since), shop_url = values(shop_url)
#                 '''
#
#                 cursor1.executemany(sql, self.item1)
#
#                 conn1.commit()
#
#                 self.count1 += 10
#                 print('-----插入完成，总数据量：%s条' % self.count1)
#
#                 self.item1 = []
#
#                 # 关闭连接
#                 cursor1.close()
#                 conn1.close()
#
#
#
#         elif isinstance(item, EbayItemGood):
#
#             # 商品表连接
#             conn2 = pymysql.Connect(host='49.235.104.232', port=3306, user='root', passwd='root', db='goods',
#                                          charset='utf8')
#             cursor2 = conn2.cursor()
#
#             data = (item['good_id'], item['good_name'], item['price_dollar'], item['price_RMB'], item['project_location'], item['brand'], item[
#                 'seller_name'], item['sales_count'], item['cat_1'], item['cat_2'], item['cat_3'], item['cat_4'], item['cat_5'], item['cat_6'])
#
#             self.item2.append(data)
#
#             if len(self.item2) == 50:
#                 print('------------开始插入商品数据-------------')
#                 sql = '''
#                     insert into goodsinfo
#                     values
#                     (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                     on duplicate key update
#                     good_id = values(good_id), good_name = values(good_name), price_dollar = values(price_dollar), price_RMB = values(price_RMB), project_location = values(project_location), brand = values(brand), seller_name = values(seller_name), sales_count = values(sales_count), cat_1 = values(cat_1), cat_2 = values(cat_2), cat_3 = values(cat_3), cat_4 = values(cat_4), cat_5 = values(cat_5), cat_6 = values(cat_6)
#                 '''
#
#                 cursor2.executemany(sql, self.item2)
#
#                 conn2.commit()
#
#                 self.count2 += 50
#                 print('-----插入完成，总数据量：%s条' % self.count2)
#
#                 self.item2 = []
#
#                 # 关闭连接
#                 cursor2.close()
#                 conn2.close()
#
#         return item

#
    # def close_spider(self, spider):
    #     pass