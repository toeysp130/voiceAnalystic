from pymongo import MongoClient

def save_data_to_mongodb(data_list):
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    collection = db['mycollection']
    collection.insert_many(data_list)
