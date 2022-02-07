import os
from dotenv import load_dotenv
from mongoengine import connect as _connect, disconnect as _disconnect

_ = load_dotenv()


def connect():
    _connect(host=os.getenv("MONGO_CONNECTION_STRING"))


def disconnect():
    _disconnect()
