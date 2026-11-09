from fastapi import FastAPI
import platform
import sys

app = FastAPI()

@app.get("/os_version")
async def get_os_version():
    os_version = platform.platform()
    return {"os_version": os_version}

@app.get("/python_version")
async def get_python_version():
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    return {"python_version": python_version}