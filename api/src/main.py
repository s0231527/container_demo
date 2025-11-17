from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Container Demo API")

class Item(BaseModel):
    name: str
    value: int

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI in a container!"}

@app.post("/items")
def create_item(item: Item):
    return {"received": item}
