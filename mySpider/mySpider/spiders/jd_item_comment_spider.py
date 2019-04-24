import json

import scrapy
from mySpider.items import JD_item, JD_comment_info
from mySpider.settings import COMMENT_URL


class Jd_item_comment_spider(scrapy.Spider):
    name = "jd_spider"
    allowed_domains = ['item.jd.com', 'sclub.jd.com']
    item_id = 6138112
    start_urls = ["http://item.jd.com/%d.html" % (item_id)]

    def parse(self, response):
        item = JD_item()
        title = response.xpath("//title/text()").extract()
        print("=======title===========", title)
        item['title'] = title
        item['jD_comment_info'] = []
        item['is_write'] = False
        page = 0
        while True:
            request = scrapy.Request(url=COMMENT_URL % (self.item_id, page), callback=self.parse_comment,
                                     meta={'item': item})
            page = page + 1

            yield request
            if item['is_write']:
                break

    def parse_comment(self, response):
        print("*" * 50)
        item = response.meta['item']
        infos = item['jD_comment_info']
        text = response.text
        json = self.parse_to_json(text)
        comments = json.get('comments')

        if comments is not None and len(comments) == 10:
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
                infos.append(info)

            item['jD_comment_info'] = infos
        else:
            item['is_write'] = True
        # item = JD_item()
        yield item

    def parse_to_json(self, str):

        str = str.replace('fetchJSON_comment98vv89(', '').replace(");", "")
        # open("jd_item_comment.txt","w").write(str)
        result = json.loads(str)
        return result
