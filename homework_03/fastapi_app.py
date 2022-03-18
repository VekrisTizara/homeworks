from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/ping/")
def ping():
    return {"message":"pong"}

@app.get("/cat", responses={200: {"content" : {"image/png" : {}}}})
def image_endpoint():
    file_path = "cat.png"
    return FileResponse(file_path, media_type="image/png", filename="cat.png")
