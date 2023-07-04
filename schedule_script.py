import subprocess
import time
import datetime

def start_fastapi_server():
    subprocess.Popen(["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])


def execute_scheduled_script():
    while True:
        now = datetime.datetime.now()
        if now.hour == 19 and now.minute == 0:
            subprocess.run(["python", "dowloaddata.py"])
            time.sleep(60)  
        else:
            time.sleep(30)  

if __name__ == "__main__":
    start_fastapi_server()
    execute_scheduled_script()