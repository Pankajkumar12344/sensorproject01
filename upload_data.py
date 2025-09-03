from pymongo.mongo_client import MongoClient
import pandas as pd

import json

url ="mongodb+srv://pankaj:KuScvnivhYzKd9hS@cluster0.0b6bfy2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client =MongoClient(url)

DATABASE_NAME="pwskills"
COLLECTION_NAME ='Waferfault'

df=pd.read_csv("C:\Users\panka\Downloads\sensorproject\notesbooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record =list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)