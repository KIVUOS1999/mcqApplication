import pymongo
from pymongo import MongoClient


def create_conn(PASSWORD="ss123546"):
    cluster = MongoClient(
        f"mongodb://kivuos:{PASSWORD}@product-shard-00-00.jlzub.mongodb.net:27017,product-shard-00-01.jlzub.mongodb.net:27017,product-shard-00-02.jlzub.mongodb.net:27017/?ssl=true&replicaSet=atlas-1ulp6q-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = cluster["mcqApplication"]
    shard = db["datas"]
    return shard


def create_payload(question, option_arr, answer):
    return (
        {
            "question": question,
            "option_arr": option_arr,
            "answer": answer
        }
    )


def add_data(obj):
    shard = create_conn()
    shard.insert_many(obj)
