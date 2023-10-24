import pymongo
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI_TBM = os.getenv("MONGO_URI_TBM")
MONGO_USERNAME_TBM = os.getenv("MONGO_USERNAME_TBM")
MONGO_PASSWORD_TBM = os.getenv("MONGO_PASSWORD_TBM")
DB_NAME_TBM = os.getenv("DB_NAME_TBM")

connection_string = f"mongodb+srv://{MONGO_USERNAME_TBM}:{MONGO_PASSWORD_TBM}@{MONGO_URI_TBM}/"
client = pymongo.MongoClient(connection_string)
db_TBM = client.get_database(DB_NAME_TBM)


def get_orders_data(db):
    collection = db["orders"]
    data = collection.find()
    orders = pd.DataFrame(data)
    return orders