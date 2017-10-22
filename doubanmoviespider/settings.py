# -*- coding: utf-8 -*-

# Scrapy settings for doubanmoviespider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanmoviespider'

SPIDER_MODULES = ['doubanmoviespider.spiders']
NEWSPIDER_MODULE = 'doubanmoviespider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanmoviespider (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"  # 默认: "Scrapy/VERSION (+http://scrapy.org)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 拒绝遵守 Robot协议 ！

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32  # 默认是16，一次可以请求的最大次数

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3  # 下载延迟
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False  # 禁用cookies

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False  # Telnet终端(Telnet Console)

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doubanmoviespider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'doubanmoviespider.middlewares.MyCustomDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 543,
     'doubanmoviespider.middlewares.MyproxiesSpiderMiddleware': 125  # None关闭代理ip中间件
}
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'doubanmoviespider.pipelines.DoubanmoviespiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGODB_HOST = '127.0.0.1'  # MONGODB 主机环回地址127.0.0.1
MONGODB_PORT = 27017  # 端口号，默认是27017
MONGODB_DBNAME = 'douban'  # 设置数据库名称
MONGODB_DOCNAME = 'movie1'  # 存放本次数据的表名称

IPPOOL = [
    {"ipaddr": "119.109.101.108:8118"},
    {"ipaddr": "183.130.63.251:80"},
    {"ipaddr": "119.90.63.3:3128"},
]
# 如果下载不了，前往下面网站收集可用ip和端口并在DOWNLOADER_MIDDLEWARES中打开代理中间件
# http://www.xicidaili.com/nt/

# 设置输出的位置和文件类型
# FEED_URI = u'file:///C:/Users/mikey/Desktop/doubanmoviespider/doubanmoviespider/items.csv'
# FEED_FORMAT = 'CSV'
