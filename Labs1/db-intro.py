from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# # 1.connect to database 
client = MongoClient(mongo_uri)

# # 2.Get Database
db = client.get_default_database()

# # 3.Create a collection
# games = db['games']

# # 4.Create a document
# new_game = {
#     "title": "Hứng bia",
#     "description":"Best game ever"
# }

# # 5.Insert doc into collection
# games.insert_one(new_game)

# # 6.Read all Documents
# all_game = games.find()
# first_game = all_game[0]
# print (first_game['title'])