import pymongo
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI_DOCPOD = os.getenv("MONGO_URI_DOCPOD")
MONGO_USERNAME_DOCPOD = os.getenv("MONGO_USERNAME_DOCPOD")
MONGO_PASSWORD_DOCPOD = os.getenv("MONGO_PASSWORD_DOCPOD")
DB_NAME_DOCPOD = os.getenv("DB_NAME_DOCPOD")

connection_string = f"mongodb+srv://{MONGO_USERNAME_DOCPOD}:{MONGO_PASSWORD_DOCPOD}@{MONGO_URI_DOCPOD}/"
client = pymongo.MongoClient(connection_string)
db_docpod = client.get_database(DB_NAME_DOCPOD)


def get_categories_data(db_docpod):
    collection = db_docpod["categories"]
    data = collection.find()
    categories = pd.DataFrame(data)
    return categories


def get_customers_data(db_docpod):
    collection = db_docpod["customers"]
    data = collection.find()
    customers = pd.DataFrame(data)
    return customers


def get_documents_data(db_docpod):
    collection = db_docpod["documents"]
    data = collection.find()
    documents = pd.DataFrame(data)
    return documents


def get_plans_data(db_docpod):
    collection = db_docpod["plans"]
    data = collection.find()
    plans = pd.DataFrame(data)
    return plans


def get_subscription_plan_data(db_docpod):
    collection = db_docpod["subscription_plan"]
    data = collection.find()
    subscription_plan = pd.DataFrame(data)
    return subscription_plan