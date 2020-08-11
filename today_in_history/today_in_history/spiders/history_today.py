import scrapy
from datetime import datetime
from ..items import TodayInHistoryItem as HistoryItem


class HistoryTodaySpider(scrapy.Spider):
    name = 'history_today'
    allowed_domains = ['zh.wikipedia.org/wiki']
    month = datetime.now().month
    day = datetime.now().day
    start_urls = [f'https://zh.wikipedia.org/wiki/{month}月{day}日']

    def parse(self, response):
        item_list = response.xpath('//h3/following-sibling::ul[1]/li')
        for item in item_list:
            historyitem = HistoryItem()
            text_list = item.css('::text').getall()
            historyitem['年份'] = text_list[0]
            historyitem['事件'] = ''.join(text_list[1:])
            yield historyitem
