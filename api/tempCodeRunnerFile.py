from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Server is up and running"


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
