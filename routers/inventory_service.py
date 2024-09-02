# routers/items.py
from fastapi import APIRouter
from kafka import KafkaConsumer, KafkaProducer
import json

router = APIRouter()

@router.on_event("startup")
async def startup_event():
    consumer = KafkaConsumer('inventory-check', bootstrap_servers=['localhost:29092'])
    producer = KafkaProducer(bootstrap_servers=['localhost:29092'])
    
    for message in consumer:
        print(message.value.decode())