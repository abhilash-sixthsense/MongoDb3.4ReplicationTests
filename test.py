from threading import Timer
import pymongo
from time import sleep


print('hi')


# myclient = pymongo.MongoClient(
#     "mongodb://localhost:40001/", replicaset='myrepl')
myclient = pymongo.MongoClient(
    ["mongodb://localhost:40001/", "mongodb://localhost:40002/", "mongodb://localhost:40003/"])
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
print(myclient.list_database_names())


def insert():
    for _ in range(1):
        mydict = {"name": "John", "address": "Highway 37"}
        x = mycol.insert_one(mydict)


def query():
    print(mycol.count_documents({}))


if __name__ == '__main__':
    while(True):
        try:
            # insert()
            query()

        except Exception as e:
            print(e)
        finally:
            sleep(2)
