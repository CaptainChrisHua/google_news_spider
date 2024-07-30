# -*- coding:utf-8 -*-
from pymongo import MongoClient
from urllib.parse import quote_plus


class MongoUtil:

    def __init__(self, config):
        host = config.get("host")
        port = config.get("port")
        database = config.get("db")
        username = config.get("username")
        password = config.get("password")
        uri = f"mongodb://{quote_plus(username)}:{quote_plus(password)}@{host}:{port}/{database}"
        self.client = MongoClient(uri, uuidRepresentation="standard")
        self.db = self.client[database]

