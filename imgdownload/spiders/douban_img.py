import scrapy
from ..items import DoubanImgsItem


class DoubanImgSpider(scrapy.Spider):
    name = 'douban_img'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/']

    def parse(self, response):
        # 正在热映的图片和电影名称, 可以改为单个item对应一张图片的方式
        img_list = response.css('#screening img::attr(src)').getall()
        img_names = response.css('#screening img::attr(alt)').getall() 
        if img_list:
            item = DoubanImgsItem()
            item['image_urls'] = img_list
            item['image_names'] = img_names
            yield item
