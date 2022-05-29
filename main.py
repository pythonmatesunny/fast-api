from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title : str
    body : str
    published :Optional[bool]




@app.get('/blog')
def index(limit : int = 0,published : bool =False):
    print(published)
    return f"hello {limit}"

@app.get('/comments/{id}')
def comments(id :int, limit :int=10):
    return f"id-{id} limit={limit}"

@app.post('/blog/')
def postblog(request:Blog):
    print(request)
    return request