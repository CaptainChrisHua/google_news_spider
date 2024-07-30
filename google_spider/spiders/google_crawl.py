# -*- coding:utf-8 -*-
import json
import os
import pathlib
import sys
from typing import Any
from urllib.parse import quote

import scrapy
from scrapy.http import Response

current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取项目根目录的路径
root_dir = os.path.join(current_dir, '..', '..', '..')

# 将项目根目录添加到sys.path
sys.path.append(root_dir)

from utils import logger


class Google2Spider(scrapy.Spider):
    name = "google2"
    allowed_domains = ["www.google.com"]
    keyword = os.environ.get("KEYWORD") or "Nvidia"
    start_year = 2014
    end_year = 2024
    n = 1
    start_urls = [f"https://www.google.com/search?q={quote(keyword)}&tbm=nws&&start={10 * (n - 1)}"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        logger.info(f"开始爬取【{self.keyword}】第{self.n}页数据")
        result_list = response.xpath('//*[@id="rso"]/div/div/div')
        for i in result_list:
            web_name = i.xpath("./div/div/a/div/div[2]/div[1]/span/text()").get()
            title = i.xpath('./div/div/a/div/div[2]/div[2]/text()').get()
            abstract = i.xpath('./div/div/a/div/div[2]/div[3]/text()').get()
            url = i.xpath('.//div/div/a/@href').get()
            image = i.xpath('./div/div/a/div/div[1]/div/div/img/@src').get()
            date = i.xpath('./div/div/a/div/div[2]/div[4]/span/text()').get()

            data = {
                "web_name": web_name,
                "title": title,
                "abstract": abstract,
                "url": url,
                "image": image,
                "date": date
            }
            print(data)
            with open("google.json", "a") as f:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write("\n")
        logger.info(f"完成第{self.n}页数据爬取")
        self.n += 1
        # next_page = response.xpath('//*[@id="pnnext"]/@href').get()
        yield scrapy.Request(
            f"https://www.google.com/search?q={quote(self.keyword)}&tbm=nws&&start={10 * (self.n - 1)}",
            callback=self.parse)
