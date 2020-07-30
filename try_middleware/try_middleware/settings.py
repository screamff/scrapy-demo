# Scrapy settings for try_middleware project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'try_middleware'

SPIDER_MODULES = ['try_middleware.spiders']
NEWSPIDER_MODULE = 'try_middleware.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'try_middleware (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'try_middleware.middlewares.TryMiddlewareSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'try_middleware.middlewares.TryMiddlewareDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'try_middleware.pipelines.TryMiddlewarePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 此处为新增的内容
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/500.4 (KHTML, like Gecko) Chrome/72.0.2898.68 Safari/500.4",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/506.35 (KHTML, like Gecko) Chrome/79.0.2929.49 Safari/506.35",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/525.17 (KHTML, like Gecko) Chrome/75.0.2374.12 Safari/525.17",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/502.20 (KHTML, like Gecko) Chrome/83.0.1294.76 Safari/502.20",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/516.29 (KHTML, like Gecko) Chrome/76.0.2409.0 Safari/516.29",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/523.6 (KHTML, like Gecko) Chrome/83.0.1536.63 Safari/523.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/500.13 (KHTML, like Gecko) Chrome/77.0.1269.65 Safari/500.13",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/521.14 (KHTML, like Gecko) Chrome/83.0.1370.74 Safari/521.14",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/524.6 (KHTML, like Gecko) Chrome/72.0.1675.67 Safari/524.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/517.16 (KHTML, like Gecko) Chrome/81.0.2438.76 Safari/517.16",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/81.0.2920.44 Safari/534.17",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/534.29 (KHTML, like Gecko) Chrome/71.0.1100.71 Safari/534.29",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/515.6 (KHTML, like Gecko) Chrome/73.0.1568.17 Safari/515.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/523.3 (KHTML, like Gecko) Chrome/71.0.2964.47 Safari/523.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/504.26 (KHTML, like Gecko) Chrome/75.0.2092.36 Safari/504.26",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/516.13 (KHTML, like Gecko) Chrome/70.0.1332.110 Safari/516.13",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/520.21 (KHTML, like Gecko) Chrome/78.0.1835.52 Safari/520.21",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/527.3 (KHTML, like Gecko) Chrome/71.0.1859.27 Safari/527.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/509.6 (KHTML, like Gecko) Chrome/73.0.2198.36 Safari/509.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/511.34 (KHTML, like Gecko) Chrome/83.0.1392.2 Safari/511.34"
]