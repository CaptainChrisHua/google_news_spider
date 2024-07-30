## Google News Spider



#### ①项目介绍 Introduction

谷歌新闻爬虫。输入新闻关键词，爬取Google新闻，存储到本地json文件

Google news crawler. Input news keywords, crawl Google news, store to local json file



#### ② 环境安装 Installation

进入项目根目录  Go to the project root directory

```shell
pip install -r requirements.txt
```



#### ③ 项目启动 Initiation

##### 1. 环境变量中配置爬取关键词

##### Configure crawling keywords in environment variables

```python
# eg:
KEYWORD=金融
```



##### 2. 日志配置

##### Log Configuration

```shell
# 默认日志路径 Default Log Path
LOG_PATH=./logs/google/
```



##### 3. 启动爬虫 

##### Start the crawler

```shell
# 1. 直接运行main.py  run main.py directly

# 2. 命令行执行 command-line execution
scrapy runspider google_spider/spiders/google_crawl.py
```

当前爬取数据存储到本地json文件中 The current crawl data is stored in a local json file



#### ④ 数据样例 Sample data

![image-20240503230355969](./assets/image-20240503230355969.png)