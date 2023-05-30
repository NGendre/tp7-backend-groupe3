from fastapi import FastAPI, APIRouter, Depends, status
import uvicorn

from src.routers.admin.users import AdminUserRouter

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


AdminRouter = APIRouter(
    prefix="/admin", tags=["admin"]
)


ItemsRouter = APIRouter(
    prefix="/items", tags=["items"]
)


@ItemsRouter.get("/")
def qszd():
    pass


''''
/admin/users
/admin/items
/admin/cities
'''


app.include_router(AdminUserRouter, prefix="/admin")
app.include_router(ItemsRouter, prefix="/admin")

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)