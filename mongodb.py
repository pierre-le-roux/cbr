from pymongo import MongoClient
import pandas as pd

class cbr:
    
    def __init__(self, database):
        self.database = database
        self.get_mongodb(database)
        self.get_data()
        
    def get_data(self):
        self.machine = self.get_collection(self.db, 'machine')
        self.grinder = self.get_collection(self.db, 'grinder')
        self.roastery = self.get_collection(self.db, 'roastery')
        self.coffee = self.get_collection(self.db, 'coffee')
        self.purchase = self.get_collection(self.db, 'purchase')
        self.recipe = self.get_collection(self.db, 'recipe')

    def get_mongodb(self):
        client = MongoClient("mongodb+srv://Roudrin:NStVHLCOw8qD54Qo@cbr-cluster.cbvbvby.mongodb.net/?retryWrites=true&w=majority")
        self.db = client[self.database]

    def get_collection(self, collection):
        collection = self.db[collection]
        return pd.DataFrame(list(collection.find()))

    def write_data(self, collection, dict):
        self.db[collection].insert_one(dict)