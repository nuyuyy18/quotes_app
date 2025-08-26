from fastapi import FastAPI
from quote import main

app = FastAPI()

@app.get("/")
async def halo():
    return {"Hello world": "anything"}

@app.get("/quotes")
async def get_quotes():
    return {"quotes": main()}

