from fastapi import FastAPI

app = FastAPI()

hashmap = dict[str, str]


@app.get("/")
async def root() -> hashmap:
    return {"message": "Hello World"}
