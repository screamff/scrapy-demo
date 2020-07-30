# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from .settings import IMAGES_STORE
from scrapy.exceptions import DropItem
from pathlib import Path


class TutorialPipeline:
    def process_item(self, item, spider):
        return item

class DoubanImgDownloadPipeline(ImagesPipeline):

    # def file_path(self, request, response=None, info=None):
    #     """可以在此处修改图片保存路径"""
    #     return super().file_path(request, response=response, info=info)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no files")

        # 以下为重命名图片部分, 如果不是批量下载, 可以在file_path方法中修改
        # for path, name in zip(image_paths, item['image_names']):
        #     oldpath = Path(IMAGES_STORE) / path
        #     newpath = Path(IMAGES_STORE) / 'full' / f'{name}.jpg'
        #     oldpath.rename(newpath)
        return item
