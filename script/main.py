import requests
import time

while True:
    try: 
        #response = requests.get('http://162.19.204.28:8000/statistics')
        response = requests.get('http://app-service/statistics')
        print(response.text)
        with open("statistics.txt", "a") as file:
            file.write(response.text + '\n')
        time.sleep(5)
    except Exception as e:
        print(e)
        time.sleep(5)
