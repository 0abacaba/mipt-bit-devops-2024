from fastapi import FastAPI
import datetime

app = FastAPI()

counter = 0
    

@app.get("/time")
async def root():
    global counter
    counter += 1
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.get("/statistics")
async def root1():
    global counter
    return str(counter)
