from fastapi import FastAPI, APIRouter, Depends, status

UsersRouter = APIRouter(
    prefix="/users", tags=["users"]
)

@UsersRouter.get("/")
def aze():
    pass
