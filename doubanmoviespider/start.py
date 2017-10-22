# -*- coding: utf-8 -*-
from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'doubanmoviespider'])
# execute(['scrapy', 'crawl', 'doubanmoviespider', '--nolog'])  # 设置无日志
# execute(['scrapy', 'crawl', 'doubanmoviespider', '-o', 'items.json', '-t', 'json'])  # 设置输出的位置和文件类型

