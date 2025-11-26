from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import sqlite3
from fastapi import UploadFile
from csv_file import handling_csv_file
import connection


app = FastAPI()

@app.post("/upload-csv")
def upload_csv(file:UploadFile):
    our_file = handling_csv_file.extract_csv(file)
    return our_file

























if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)
