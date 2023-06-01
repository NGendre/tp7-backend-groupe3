from fastapi import FastAPI

import uvicorn

from src.models.BaseModel import init
from src.routers.admin.items.AdminItemRouter import ItemRouter
from src.routers.admin.users.AdminUserRouter import UsersRouter


app = FastAPI()
app.include_router(UsersRouter, prefix="/admin", tags=["admin"])
app.include_router(ItemRouter, prefix="/admin", tags=["admin"])
init()

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)

