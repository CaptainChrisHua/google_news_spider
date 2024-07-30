# -*- coding:utf-8 -*-
import os
import sys
from typing import Any

import scrapy
from pymongo import InsertOne
from pymongo.errors import BulkWriteError
from scrapy.http import Response

current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取项目根目录的路径
root_dir = os.path.join(current_dir, '..', '..', '..')

# 将项目根目录添加到sys.path
sys.path.append(root_dir)

from utils import logger, mongo


class GoogleSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["www.google.com"]
    keyword = "WTI Crude Oil"
    start_urls = [
        f"https://www.google.com/search?q=%E5%8E%9F%E6%B2%B9&sca_esv=c737185ccb2b48d3&tbm=nws&sxsrf=ACQVn0-OiJb8IfE9kOStgBdQSVfHmA0Z8g:1708749617064&source=lnt&sa=X&ved=2ahUKEwiWrb2vlMOEAxWTJUQIHTaDCp8QpwV6BAgBEA4&tbas=0&biw=1382&bih=745&dpr=2"]
    n = 0

    def save_to_mongo(self, doc_list):
        operations = []
        for data in doc_list:
            operation = InsertOne(data)
            operations.append(operation)
        try:
            mongo.db["utc_chat_news"].bulk_write(operations)
        except BulkWriteError as e:
            logger.info("批量写入错误")

    def parse(self, response: Response, **kwargs: Any) -> Any:
        # 1. 打开页面，爬取页面中所有标题，url，摘要，去掉赞助商
        # 2. 翻页，继续爬取
        # 3.
        # self.n += 1
        # logger.info(f"开始爬取第{self.n}页数据")
        result_list = response.xpath('//*[@id="rso"]/div/div/div')

        data_list = []
        for i in result_list:
            web_name = i.xpath("./div/div/a/div/div[2]/div[1]/span/text()").get()
            title = i.xpath('./div/div/a/div/div[2]/div[2]/text()').get()
            abstract = i.xpath('./div/div/a/div/div[2]/div[3]/text()').get()
            url = i.xpath('.//div/div/a/@href').get()
            image = i.xpath('./div/div/a/div/div[1]/div/div/img/@src').get()
            release_time = i.xpath('./div/div/a/div/div[2]/div[4]/span/text()').get()

            # match = re.search(r"/item/([^/]+)/(\d+)", response.url)
            # topic = unquote(match.group(1))
            # topic_id = match.group(2)
            # raw_summary = response.xpath('//div[contains(@class, "J-summary")]//text()').extract()
            # cleaned_summary = [re.sub(r' \[\d+\]|\[\d+\]|\n|\xa0', '', item) for item in raw_summary]
            # summary = ''.join(cleaned_summary)

            news = dict(
                key_word=self.keyword,
                web_name=web_name,
                title=title,
                abstract=abstract,
                url=url,
                image=image,
                release_time=release_time,
                source="Google",
            )
            data_list.append(news)
        print(data_list)
        # self.save_to_mongo(data_list)
        logger.info(f"完成{self.keyword}数据爬取")
        # logger.info(f"完成第{self.n}页数据爬取")
        # next_page = response.xpath('//*[@id="pnnext"]/@href').get()
        # if next_page:
        #     yield response.follow(next_page, self.parse)
        return data_list
        # todo 更换ip
        # todo 登录
        # todo 破解转动验证码
