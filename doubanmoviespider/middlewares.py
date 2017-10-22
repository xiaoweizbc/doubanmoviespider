# -*- coding: utf-8 -*-
import random
from doubanmoviespider.settings import IPPOOL


class MyproxiesSpiderMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        print("this is ip:" + thisip["ipaddr"])
        request.meta["proxy"] = "http://" + thisip["ipaddr"]
