import uvicorn
from fastapi import FastAPI
from data.newsgroups_data import NewsgroupsData
from kafka_utils import get_producer_config, publish_message

app = FastAPI()


data = NewsgroupsData()
data.get_data()


producer = get_producer_config()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/interesting")
async def publish_interesting():
    for msg in data.interesting:
        publish_message(producer, "interesting", {"text": msg})
    producer.flush()
    return {"status": "sent", "topic": "interesting", "count": len(data.interesting)}

@app.get("/not_interesting")
async def publish_not_interesting():
    for msg in data.not_interesting:
        publish_message(producer, "not_interesting", {"text": msg})
    producer.flush()
    return {"status": "sent", "topic": "not_interesting", "count": len(data.not_interesting)}


