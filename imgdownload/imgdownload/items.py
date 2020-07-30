# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class ImgdownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanImgsItem(scrapy.Item):
    # 前两个为必要字段
    image_urls = Field()
    images = Field()
    image_names = Field()