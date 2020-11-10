import pymongo


try:
    mongo = pymongo.MongoClient(host='localhost', port = 27017, serverSelectionTimeoutMS = 1000)
    db = mongo.company
    mongo.server_info()
    print("Mongodb connection successfull")

except:
    print("Mongodb connection error!!")