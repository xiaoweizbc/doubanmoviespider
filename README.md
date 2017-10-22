#说明
###创建项目
```
scrapy startproject doubanmoviespider
```
###定义Item
#####编辑doubanmoviespider目录下的items.py文件：
```
import scrapy
class DoubanmoviespiderItem(scrapy.Item):
    id = scrapy.Field()  # 电影id
    title = scrapy.Field()  # 电影标题
    content = scrapy.Field()  # 电影信息
    score = scrapy.Field()  # 电影评分
    quote = scrapy.Field()  # 简介
    url = scrapy.Field()  # 电影url，用于翻页爬取下面的电影photo
    photo = scrapy.Field()  # 电影photo
```
###编写爬虫(Spider)
#####在doubanmoviespider/spiders目录下新建spider.py文件：
```
代码略：实现了多页爬取和层级爬取
```
###编写item pipeline将爬取结果保存到mongodb数据库中
#####编辑doubanmoviespider目录下的pipelines.py文件：
```
代码略：实现了将item写入mongodb数据库
```
###编写代理ip爬虫中间件
#####在doubanmoviespider/spiders目录下新建spider.py文件：
```
import random
from doubanspider.settings import IPPOOL
class MyproxiesSpiderMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        print("this is ip:" + thisip["ipaddr"])
        request.meta["proxy"] = "http://" + thisip["ipaddr"]
```
###爬取
#####1.进入项目的根目录，执行下列命令启动spider:
```
scrapy crawl doubanmoviespider
```
#####2.用python运行文件start.py
```
python start.py
```



#附：其余说明在各文件代码中注释