from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI running 🚀",
        "container": socket.gethostname(),
        "server_name": os.getenv("SERVER_NAME", "unknown")
    }