import requests
import base64

auth = base64.b64encode(b"lucas:admin").decode("utf-8")
headers = { "Authorization": f"Basic {auth}"} 

def popular_banco():
    posts = [
        {
        "name": "Pessoa 1",
        "date": "2023-03-2",
        "hour": "15:00",
        "email": "lucasmaxgames@gmail.com",
        "healthInsurance": "",
        "telephone": "3391287475"
        },
        {
        "name": "Pessoa 2",
        "date": "2023-03-1",
        "hour": "15:00",
        "email": "lucasmaxgames@gmail.com",
        "healthInsurance": "",
        "telephone": "3391287475"
        },
        {
        "name": "Pessoa 3",
        "date": "2023-03-28",
        "hour": "15:00",
        "email": "lucasmaxgames@gmail.com",
        "healthInsurance": "",
        "telephone": "3391287475"
        },
        {
        "name": "Pessoa 4",
        "date": "2023-03-26",
        "hour": "15:00",
        "email": "lucasmaxgames@gmail.com",
        "healthInsurance": "",
        "telephone": "3391287475"
        },
        {
        "name": "Pessoa 5",
        "date": "2023-03-21",
        "hour": "15:00",
        "email": "lucasmaxgames@gmail.com",
        "healthInsurance": "",
        "telephone": "3391287475"
        },
        {
        "name": "Pessoa 6",
        "date": "2023-03-20",
        "hour": "15:00",
        "email": "lucasmaxgames@gmail.com",
        "healthInsurance": "",
        "telephone": "3391287475"
        },
        {
        "name": "Pessoa 7",
        "date": "2023-03-22",
        "hour": "15:00",
        "email": "lucasmaxgames@gmail.com",
        "healthInsurance": "",
        "telephone": "3391287475"
        },
    
    ]
    for post in posts:
        response = requests.post("http://127.0.0.1:8000/schedules/",data=post, headers=headers)
        #status = response.status_code
        #response = response.json()
        #response["status"] = status
        print(response)

popular_banco()