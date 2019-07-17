import pymongo 

mongo_client=pymongo.MongoClient('localhost',27017)

db=mongo_client.myDB
my_collection=db.myCollection
# my_collection=db['myCollection']


print("="*50)

tom={'name':'Tom','age':18,'sex':'男','hobbies':['吃饭','睡觉','打豆豆']}
alice={'name':'Alice','age':19,'sex':'女','hobbies':['读书','跑步','弹吉他']}
tom_id=my_collection.insert(tom)
alice_id=my_collection.insert(alice)
print(tom_id)
print(alice_id)


print("="*50)
cursor=my_collection.find()
print(cursor.count()) 
for item in cursor:
    print(item)


print("="*50)
my_collection.update({'name':'Tom'},{'$set':{'hobbies':['向Alice学习读书','跟Alice一起跑步','向Alice学习弹吉他']}})
for item in my_collection.find():
    print(item)


print("="*50)
my_collection.remove({'name':'Tom'},{'justOne':0})
my_collection.remove()
for item in my_collection.find():
    print(item)
