from pymongo import MongoClient
import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd

load_dotenv(Path(os.getcwd()) / 'secrets.env')

class CBR:
    
    def __init__(self, database):
        self.database = database
        self.get_mongodb()
        self.get_data()
        self.collections =  [self.machine, self.grinder, self.roastery, 
                             self.coffee, self.purchase, self.recipe]
        
    def get_data(self):
        self.machine = self.get_collection('machine')
        self.grinder = self.get_collection('grinder')
        self.roastery = self.get_collection('roastery')
        self.coffee = self.get_collection('coffee')
        self.purchase = self.get_collection('purchase')
        self.recipe = self.get_collection('recipe')
        
    def print_all_data(self):
        for collection in self.collections:
            print(collection.shape)
            # print(collection.head())

    def get_mongodb(self):
        client = MongoClient(f"mongodb+srv://{os.getenv('MONGOUSR')}:{os.getenv('MONGOPWD')}@cbr-cluster.cbvbvby.mongodb.net/?retryWrites=true&w=majority")
        self.db = client[self.database]

    def get_collection(self, collection):
        collection = self.db[collection]
        return pd.DataFrame(list(collection.find()))

    def write_data(self, collection, dict):
        self.db[collection].insert_one(dict)
        
    def add_data(self):
        for column in collection.columns.drop("_id"):
            print(column)