from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import db_utils
import json

app = FastAPI()

@app.get("/")
def redirect():
    return RedirectResponse("/docs")

@app.post("/shorten", status_code=201)
def add_item(url: str) -> str:
    return db_utils.insert_url(url)

@app.get("/{url}")
def get_original_url(url: int):
    url = db_utils.get_original_url(url)
    if (url == None):
        return HTTPException(404)
    return RedirectResponse(url[0])
    
@app.get("/stats/{short_id}")
def get_url_data(short_id: int):
    url = db_utils.get_original_url(short_id)
    if (url == None):
        return HTTPException(404)
    return url
