from fastapi import FastAPI, APIRouter, Depends, status


AdminRouter = APIRouter(
    prefix="/admin", tags=["admin"]
)



''''
/admin/users
/admin/items
/admin/cities
'''
