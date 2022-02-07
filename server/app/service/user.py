from fastapi import APIRouter
from app.db import db_manager
from app.service.model import UserModel

route = APIRouter(prefix="/user", tags=["user"])


@route.post("/")
def create_user(user: UserModel):
    return db_manager.add_user(user)


@route.get("/")
def get_users():
    return db_manager.get_users()


@route.get("/{id}")
def get_user(id: str):
    return db_manager.get_user(id)
