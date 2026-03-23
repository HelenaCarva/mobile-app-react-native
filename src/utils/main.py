import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from uvicorn import run
from pydantic import BaseModel
from typing import Optional
import asyncio
import json
from datetime import datetime

load_dotenv()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/configs")
async def read_config():
    return {"message": "Server is running"}

@app.get("/api/timestamp")
async def get_timestamp():
    return {"timestamp": str(datetime.now())}

@app.get("/api/logs")
async def get_logs():
    try:
        with open ("logs.txt", "r") as f:
            return {"logs": f.read()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/{file}")
async def read_file(file: str):
    try:
        return FileResponse(file)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True)