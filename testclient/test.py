from threading import Timer
import pymongo
from time import sleep

print('Running Test')

#c = pymongo.Connection("repl1:27017", slave_okay=True)

print('Creating Connection ...')


# myclient = pymongo.MongoClient(
#["mongodb://127.0.0.1:40001/", "mongodb://127.0.0.1:40002/", "mongodb://127.0.0.1:40003/"])

myclient = pymongo.MongoClient(
    ["mongodb://repl1:27017/", "mongodb://repl2:27017/", "mongodb://repl3:27017/"])
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
print(myclient.list_database_names())
print('Completed Creating Connection ...')

def insert():
    for _ in range(1):
        print('Inserting ...')
        mydict = {"name": "John", "address": "Highway 37"}
        x = mycol.insert_one(mydict)


def query():

    print(mycol.count_documents({}))


if __name__ == '__main__':
    while(True):
        try:
            insert()
            print('Running Query')
            query()

        except Exception as e:
            print(e)
        finally:
            sleep(2)
