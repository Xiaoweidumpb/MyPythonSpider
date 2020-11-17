# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class MaoyanProjectPipeline:
    MONGO_URL = '212.64.70.92'
    MONGO_PORT = 27017
    MONGO_DB = "maoyan_rank"  # 库名
    MONGO_COLL = "weimingzhong"  # collection名
    # @classmethod
    # def from_crawler(cls, crawler):
    #     """
    #     1、读取settings里面的mongodb数据的url、port、DB。
    #     """
    #     return cls(
    #         mongourl=crawler.settings.get("MONGO_URL"),
    #         mongoport=crawler.settings.get("MONGO_PORT"),
    #         mongodb=crawler.settings.get("MONGO_DB")
    #     )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.MONGO_URL, self.MONGO_PORT)
        self.db = self.client[self.MONGO_DB]
    def process_item(self, item, spider):
        # name = item.__class__.__name__
        self.db[self.MONGO_COLL].insert_one(item)
        return item
    def close_spider(self, spider):
        self.client.close()
