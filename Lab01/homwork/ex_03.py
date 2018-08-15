from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()

new_post = {
    'title': 'Captain',
    'author': 'Anh Vu',
    'content': 'I know you know'
}

db.posts.insert_one(new_post)