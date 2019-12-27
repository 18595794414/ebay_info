

BOT_NAME = 'ebayinfo'

SPIDER_MODULES = ['ebayinfo.spiders']
NEWSPIDER_MODULE = 'ebayinfo.spiders'
COMMANDS_MODULE = 'ebayinfo.commands'

# 禁用机器协议
ROBOTSTXT_OBEY = False

# 下载超时时间
DOWNLOAD_TIMEOUT = 30

# 日志级别
# LOG_LEVEL = 'INFO'

# 开启重试：
RETRY_ENABLED = True

# 重试次数
RETRY_TIMES = 3

# 同一时间最大请求数
CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 禁用cookie
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}


# SPIDER_MIDDLEWARES = {
#    'ebayinfo.middlewares.EbaySpiderMiddleware': 543,
# }


DOWNLOADER_MIDDLEWARES = {
   # 'ebayinfo.middlewares.EbayinfoDownloaderMiddleware': 543,
}


# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }


ITEM_PIPELINES = {
   'ebayinfo.pipelines.SavePipeline': 300,

}


# 开启自动限速
AUTOTHROTTLE_ENABLED = True

# 开始下载时限速并延迟时间
AUTOTHROTTLE_START_DELAY = 1

# 高并发请求时最大延迟时间
AUTOTHROTTLE_MAX_DELAY = 15

# 平均每秒并发数
AUTOTHROTTLE_TARGET_CONCURRENCY = 6.0

# 是否显示
# AUTOTHROTTLE_DEBUG = False

# 打开缓存
# HTTPCACHE_ENABLED = True
# 设置缓存过期时间（单位：秒）
# HTTPCACHE_EXPIRATION_SECS = 0
# 缓存路径(默认为：.scrapy/httpcache)
# HTTPCACHE_DIR = 'httpcache'
# 忽略的状态码
# HTTPCACHE_IGNORE_HTTP_CODES = []
# 缓存模式(文件缓存)
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# REDIS_URL = 'redis://192.168.0.230:6379/0'
# SCHEDULER_PERSIST = True