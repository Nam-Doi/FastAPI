from fastapi import Body, FastAPI, Response,status, HTTPException,Depends
from random import randrange
from pydantic import BaseModel
from typing import Optional,List
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from datetime import datetime
from sqlalchemy.orm import Session
from . import models,schemas,utils
from .database import engine,get_db
from .routers import post, user,auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



# cursor và conn là global
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi',user='postgres',
#                                 password='Nammount19@',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connection database failed!")
#         print("Error: ", error)
#         time.sleep(2)

# my_post = [{"id":1, "title":"Nam is the best player in the world!","content":"Arthur Chen"},
#            {"id":2,"title":"The Sun, The Moon and you", "content": "Lieu Nhu Yen"}]

# def find_id(id):
#     for i in my_post:
#         if i["id"] == id:
#             return i
#     return -1
# def find_index_id(id):
#     for i in range(len(my_post)):
#         if my_post[i]["id"] == id:
#             return i+1
#     return -1



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello, Arthur!!!"}




