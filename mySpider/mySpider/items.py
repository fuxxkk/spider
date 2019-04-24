# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    #pass

class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()

class JD_item(scrapy.Item):
    title = scrapy.Field() #标题
    jD_comment_info = scrapy.Field() #评论信息

class JD_comment_info(object):
    user = ''  # 用户
    star = 0 # 评分
    order_info = ''   # 订单信息
    order_date = None # 订单时间
    comments = []  # 评论
