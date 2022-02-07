from unittest.mock import Base
from pydantic import BaseModel


class UserModel(BaseModel):
    firstname: str
    lastanem: str
    email: str
    password: str
