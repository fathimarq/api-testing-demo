from fastapi import FastAPI

app = FastAPI()
items = []

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(name: str):
    items.append(name)
    return {"name": name, "status": "added"}
