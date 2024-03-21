from fastapi import FastAPI

from src.database import Database

app = FastAPI()

Database().verify_connection()