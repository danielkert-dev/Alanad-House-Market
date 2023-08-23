from pymongo import MongoClient
from django.conf import settings

def get_mongodb_connection(db_name):
    mongo_settings = settings.MONGO_DB
    client = MongoClient(mongo_settings['URL'])
    db = client[db_name]
    return db