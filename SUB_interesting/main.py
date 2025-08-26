import uvicorn
from fastapi import FastAPI
from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import datetime
import threading

app = FastAPI()

# MongoDB
mongo = MongoClient("mongodb://localhost:27017/")
db = mongo["newsgroups"]
collection = db["interesting"]

# Kafka Consumer
consumer = KafkaConsumer(
    "interesting",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)


def consume_messages():
    for msg in consumer:
        doc = msg.value
        doc["timestamp"] = datetime.datetime.now()
        collection.insert_one(doc)


threading.Thread(target=consume_messages, daemon=True).start()


@app.get("/messages")
async def get_messages():
    return list(collection.find({}, {"_id": 0}))

