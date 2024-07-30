# -*- coding:utf-8 -*-
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "runspider", "google_spider/spiders/google_crawl.py"])
