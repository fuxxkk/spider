# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ItcastPipeline(object):
    def __init__(self):
        self.json_file = open("teachers.json", "w")

    def process_item(self, item, spider):
        item['name']=item['name'].strip()
        # dumps()将一个Python数据结构转换为JSON
        item_json = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #print(type(item_json))
        self.json_file.write(item_json)
        return item

    def close_spider(self, spider):
        self.json_file.close()