# main.py
# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import api
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]


# Initialize the app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)


# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Chào mừng bạn đến với API"}
