import scrapy


class SeleniumspiderSpider(scrapy.Spider):
    name = 'seleniumspider'
    start_urls = ['https://dynamic5.scrape.center/']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'try_middleware.middlewares.TryMiddlewareDownloaderMiddleware': 543,
            'try_middleware.middlewares.UAMiddleware': 544,
            'try_middleware.middlewares.SeleniumMiddleware': 545
        }
    }

    def parse(self, response):
        for img in response.css('img').getall():
            yield dict(img=img)