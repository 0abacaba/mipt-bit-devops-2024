from fastapi import FastAPI
import datetime
import requests

app = FastAPI()

counter = 0
    

@app.get("/time")
async def root():
    global counter
    counter += 1
    response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    if response.status_code == 200:
        return response.json()['datetime']
    else:
        return f"Ошибка при запросе{response.status_code}"


@app.get("/statistics")
async def root1():
    global counter
    return str(counter)
