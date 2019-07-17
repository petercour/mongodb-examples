import pymongo 

mongo_client=pymongo.MongoClient('localhost',27017)

db=mongo_client.myDB
my_collection=db['myFriends']


print("="*25)
my_collection.update({'name':'Alice'},{'$set':{'hobbies':['Music']}})
for item in my_collection.find():
    print(item)


print("="*25)
my_collection.remove({'name':'Tom'})
for item in my_collection.find():
    print(item)
