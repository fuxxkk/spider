import json

import scrapy
from mySpider.items import JD_item, JD_comment_info
from mySpider.settings import COMMENT_URL


class Jd_item_comment_spider(scrapy.Spider):
    infos = []
    name = "jd_spider"
    allowed_domains = ['item.jd.com', 'sclub.jd.com']
    item_id = 6138114
    start_url = "http://item.jd.com/%d.html" % (item_id)
    start_urls = [start_url]

    def parse(self, response):
        item = JD_item()
        title = response.xpath("//title/text()").extract()
        print("=======title===========", title)
        item['title'] = title
        item['jD_comment_info'] = []
        page = 0
        request_url = COMMENT_URL % (self.item_id, page)

        # ------headers------
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-cn",
            "Connection": "keep-alive",
            # "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Referer": self.start_url
        }
        while True:
            request = scrapy.Request(url=COMMENT_URL % (self.item_id, page), callback=self.parse_comment,
                                     meta={'item': item}, headers=headers)
            page = page + 1

            yield request

    def parse_comment(self, response):
        print("*" * 50)
        item = response.meta['item']
        #infos = item['jD_comment_info']
        text = response.text


        try:
            json = self.parse_to_json(text)
            comments = json.get('comments')
            for comment in comments:
                content = comment.get('content')
                name = comment.get("nickname")
                date = comment.get('creationTime')
                score = comment.get('score')
                order_info = comment.get('productColor') + " " + comment.get('productSize')
                info = JD_comment_info()
                info['username'] = name
                info['comment'] = content
                info['order_date'] = date
                info['score'] = score
                info['order_info'] = order_info
                self.infos.append(info)

            item['jD_comment_info'] = self.infos
            # print("infos length:",len(infos))
            # item = JD_item()
            yield item
        except Exception as e:
            item = JD_item()
            item['title'] = "stop"
            yield item
            self.crawler.engine.close_spider(self, '关闭爬虫')

    def parse_to_json(self, str):

        str = str.replace('fetchJSON_comment98vv262(', '').replace(");", "")
        # open("jd_item_comment.txt","w").write(str)
        result = json.loads(str)
        return result
