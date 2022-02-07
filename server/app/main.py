from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.service import user
from app.db import connect, disconnect


app = FastAPI(
    title="chat-api",
    openapi_url="/api/v1/chat/openapi.json",
    docs_url="/api/v1/chat/docs",
)

app.include_router(user.route, prefix="/api/v1/chat")


@app.get("/")
def say_hello():
    return "hello users"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    connect()


@app.on_event("shutdown")
def shutdown():
    disconnect()
