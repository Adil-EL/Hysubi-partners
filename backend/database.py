#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import Todo

conn_str = "mongodb+srv://AdilLaptops:nUoMiKD4Gphnx2DT@laptops.m72a4.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
database = client.laptops
collection = database.partners

async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True