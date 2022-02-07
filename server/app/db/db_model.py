from mongoengine import Document, StringField, EmailField


class User(Document):
    meta = {"collection": "users"}
    firstname = StringField(required=True)
    lastanem = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
