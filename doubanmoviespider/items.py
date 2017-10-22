# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # 电影id
    title = scrapy.Field()  # 电影标题
    content = scrapy.Field()  # 电影信息
    score = scrapy.Field()  # 电影评分
    quote = scrapy.Field()  # 简介
    url = scrapy.Field()  # 电影url
    photo = scrapy.Field()  # 电影photo
