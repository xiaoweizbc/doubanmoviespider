# -*- coding: utf-8 -*-
import scrapy
from doubanmoviespider.items import DoubanmoviespiderItem
from scrapy.http import Request


class DoubanMovieSpider(scrapy.Spider):
    name = "doubanmoviespider"  # 与start.py中的命令对应的
    allowed_domains = ["movie.douban.com"]

    def start_requests(self):
        for i in range(0, 25, 25):  # 改成0, 250, 25就可以爬取全部Top250
            url = "https://movie.douban.com/top250?start=" + str(i) + "&filter="
            print url
            yield Request(url, callback=self.parse_one)

    def parse_one(self, response):
        items = []
        # < class 'scrapy.selector.unified.SelectorList'>使用extract()转成list
        movies = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for each in movies:
            item = DoubanmoviespiderItem()
            # <type 'list'>
            id = each.xpath('div/div[1]/em/text()').extract()
            title = each.xpath('div/div[2]/div[@class="hd"]/a/span/text()').extract()
            content = each.xpath('div/div[2]/div[@class="bd"]/p/text()').extract()
            score = each.xpath('div/div[2]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            quote = each.xpath('div/div[2]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            url = each.xpath('div/div[2]/div[@class="hd"]/a/@href').extract()
            item['id'] = id[0]
            item['title'] = ''.join(title)
            item['content'] = ''.join(content).replace(' ', '').replace('\n', '')
            item['score'] = score[0]
            if len(quote) == 0:
                item['quote'] = ""
            else:
                item['quote'] = quote[0]
            item['url'] = url[0]
            items.append(item)
        for item in items:
            # print item['id'], item['title'], item['content'], item['score'], item['quote'], item['url']
            yield Request(url=item['url'], meta={"item1": item}, callback=self.parse_two)

    def parse_two(self, response):
        item = DoubanmoviespiderItem()
        item2 = response.meta['item1']
        # print item2['id'], item2['title'], item2['content'], item2['score'], item2['quote'], item2['url']
        item['id'] = item2['id']
        item['title'] = item2['title']
        item['content'] = item2['content']
        item['score'] = item2['score']
        item['quote'] = item2['quote']
        item['url'] = item2['url']
        photo = response.xpath('//*[@id="mainpic"]/a/img/@src').extract()
        item['photo'] = photo[0]
        print item['id'], item['title'], item['content'], item['score'], item['quote'], item['url'], item['photo']
        yield item
