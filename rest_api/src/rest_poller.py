import os
import time
import requests

frequency = 1.0

if __name__ == "__main__":
    # To enable requests for local host
    os.environ['NO_PROXY'] = "127.0.0.1"
    
    while True:
        response = requests.get("http://127.0.0.1:7201/api/robot/status")
        print(response)
        print(response.json())
        time.sleep(1/frequency)