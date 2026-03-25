from fastapi import FastAPI, Request
import socket
import os

app = FastAPI()

@app.get("/")
def home(request: Request):
    return {
        "message": "FastAPI running 🚀",
        "container_id": socket.gethostname(),
        "server_name": os.getenv("SERVER_NAME", "unknown"),
        "client_ip": request.client.host
    }