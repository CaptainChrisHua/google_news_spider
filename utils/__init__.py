# -*- coding:utf-8 -*-
from google_spider.settings import LOG_PATH, LOG_LEVEL, MONGODB_CONFIG
from utils.log_utils import LogUtil
from utils.mongo_util import MongoUtil
from utils.mysql_util import SQLAlchemyUtil
from utils.redis_util import RedisUtil

# db = SQLAlchemyUtil(SQLALCHEMY_CONFIG, engine="postgresql+psycopg2").get_session
mongo = MongoUtil(MONGODB_CONFIG)
logger = LogUtil(log_path=LOG_PATH, log_level=LOG_LEVEL)
# redis_util = RedisUtil(REDIS_CONFIG)
# mongo = MongoUtil(MONGODB_CONFIG)

if __name__ == '__main__':
    mongo.db["utc_chat_news"].insert_one([{"haha": "hehe"}])
