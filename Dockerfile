FROM python:3.9.12-slim-buster

MAINTAINER xxx

ENV LANG=C.UTF-8

RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

COPY requirements.txt /root/project/google_spider/requirements.txt

RUN mkdir -p /root/google_spider/logs && \
pip3 install --no-cache -r /root/project/google_spider/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /root/project/google_spider
WORKDIR /root/project/google_spider

ENV PYTHONPATH=/root/project/google_spider

CMD scrapy runspider /root/project/google_spider/google_spider/spiders/google_crawl.py
