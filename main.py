from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI running 🚀",
        "container": socket.gethostname(),
        "port": os.getenv("PORT", "unknown"),
        "server_name": os.getenv("SERVER_NAME", "unknown")
    }