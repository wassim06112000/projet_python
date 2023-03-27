from pymongo import MongoClient


class Mongobdd:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def insert_data(self, data):
        self.collection.insert_many(data)


