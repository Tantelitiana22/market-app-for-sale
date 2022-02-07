from mongoengine.queryset.queryset import QuerySet
from app.db.db_model import User
from app.service.model import UserModel


def add_user(user: UserModel) -> User:
    return User(**user.dict()).save()


def get_users() -> QuerySet:
    return User.objects.all()


def get_user(id: str) -> User:
    return User.objects.get(_id=id)
