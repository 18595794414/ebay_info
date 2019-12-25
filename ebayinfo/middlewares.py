# -*- coding: utf-8 -*-
import os

from fake_useragent import UserAgent
from scrapy import signals


class EbayinfoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class EbayinfoDownloaderMiddleware(object):
    def __init__(self):
        self.ua = UserAgent()
        self.num = 0

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", self.ua.random)
        self.num += 1
        if self.num % 1000 == 0:
            # self.huan_ip()
            self.num = 0

    def connect(self):
        name = "宽带连接"
        username = 'wzg.22576911'
        password = "542861"
        cmd_str = "rasdial %s %s %s" % (name, username, password)
        res = os.system(cmd_str)
        if res == 0:
            print("连接成功")
        else:
            print(res)

    def disconnect(self):
        name = "宽带连接"
        cmdstr = "rasdial %s /disconnect" % name
        os.system(cmdstr)
        print('断开成功')

    def huan_ip(self):
        # 断开网络
        self.disconnect()
        # 开始拨号
        self.connect()

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
