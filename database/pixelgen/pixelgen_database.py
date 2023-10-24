import pymongo
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI_PIXELGEN = os.getenv("MONGO_URI_PIXELGEN")
MONGO_USERNAME_PIXELGEN = os.getenv("MONGO_USERNAME_PIXELGEN")
MONGO_PASSWORD_PIXELGEN = os.getenv("MONGO_PASSWORD_PIXELGEN")
DB_NAME_PIXELGEN = os.getenv("DB_NAME_PIXELGEN")

connection_string = f"mongodb+srv://{MONGO_USERNAME_PIXELGEN}:{MONGO_PASSWORD_PIXELGEN}@{MONGO_URI_PIXELGEN}/"
client = pymongo.MongoClient(connection_string)
db_pixelgen = client.get_database(DB_NAME_PIXELGEN)


def get_images_data(db_pixelgen):
    collection = db_pixelgen["images"]
    data = collection.find()
    images = pd.DataFrame(data)
    return images


def get_palettes_data(db_pixelgen):
    collection = db_pixelgen["palettes"]
    data = collection.find()
    palettes = pd.DataFrame(data)
    return palettes


def get_subscription_attempts_data(db_pixelgen):
    collection = db_pixelgen["subscription_attempts"]
    data = collection.find()
    subscription_attempts = pd.DataFrame(data)
    return subscription_attempts


def get_subscription_plans_data(db_pixelgen):
    collection = db_pixelgen["subscription_plans"]
    data = collection.find()
    subscription_plans = pd.DataFrame(data)
    return subscription_plans


def get_user_credits_data(db_pixelgen):
    collection = db_pixelgen["user_credits"]
    data = collection.find()
    user_credits = pd.DataFrame(data)
    return user_credits


def get_user_details_data(db_pixelgen):
    collection = db_pixelgen["user_details"]
    data = collection.find()
    user_details = pd.DataFrame(data)
    return user_details

def get_user_location_data(db_pixelgen):
    collection = db_pixelgen["user_location"]
    data = collection.find()
    user_location = pd.DataFrame(data)
    return user_location

def get_user_device_info_data(db_pixelgen):
    collection = db_pixelgen["user_device_info"]
    data = collection.find()
    user_device_info = pd.DataFrame(data)
    return user_device_info

def get_referrals_data(db_pixelgen):
    collection = db_pixelgen["referrals"]
    data = collection.find()
    referrals = pd.DataFrame(data)
    return referrals