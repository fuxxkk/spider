# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from mySpider.items import JD_comment_info,JD_item


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ItcastPipeline(object):
    def __init__(self):
        self.json_file = open("teachers.json", "w")

    def process_item(self, item, spider):
        item['name'] = item['name'].strip()
        # dumps()将一个Python数据结构转换为JSON
        item_json = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # print(type(item_json))
        self.json_file.write(item_json)
        return item

    def close_spider(self, spider):
        self.json_file.close()


class JdItemPipeline(object):
    item = JD_item()
    def __init__(self):
        self.json_file = open("items.json", "w")

    def process_item(self, item, spider):
        if item['title'] == 'stop':
            print("=" * 100)
            item_json = json.dumps(dict(self.item), ensure_ascii=False, cls=Jd_item_encoding) + "\n"
            self.json_file.write(item_json)
            self.json_file.close()
        else:
            self.item = item
        return item

    def close_spider(self, spider):
        #self.json_file.close()
        pass


class Jd_item_encoding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, JD_comment_info):
            return "{username:%s,score:%d,order_info:%s,order_date:%s,comment:%s}\n" % (
                o['username'], o['score'], o['order_info'], o['order_date'], o['comment'])
        return json.JSONEncoder.default(self, o)
