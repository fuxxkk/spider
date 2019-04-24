# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # pass


class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()


class JD_item(scrapy.Item):
    is_write = scrapy.Field()
    title = scrapy.Field()  # 标题
    jD_comment_info = scrapy.Field()  # 评论信息


class JD_comment_info(scrapy.Item):
    username = scrapy.Field()  # 用户
    score = scrapy.Field()  # 评分
    order_info = scrapy.Field()  # 订单信息
    order_date = scrapy.Field()  # 订单时间
    comment = scrapy.Field()  # 评论

    # def __str__(self):
    #     str = "{username:%s,score:%d,order_info:%s,order_date:%s,comment:%s}"%(self.username,self.score,self.order_info,self.order_date,self.comment)
    #     return str
