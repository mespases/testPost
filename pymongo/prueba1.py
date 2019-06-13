import pymongo
from pymongo import MongoClient

# "mongodb://localhost:27017/" Formato URI mongodb
# 'localhost', 27017 Nos conectamos al localhost en el puerto expecificado




"""client = pymongo.MongoClient('localhost', 27017)

db = client['test-database']

post = {
  "autor" : "Mike",
  "text" : "My first blog post",
  "tags" : ["mongodb", "python", "pymongo"]
}

posts = db.posts
post_id = db.posts.insert_one(post).insert_id
post_id """

from pymongo import MongoClient
c = MongoClient('localhost', 27017)

db = pymongo.mongo_client.Prueba1

a = c.admin.command('ping')
print a