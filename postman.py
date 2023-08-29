import requests 

data = {
    'Body':'Jaipur',
    'From':'whatsapp:+919986123781'
}
data1 = {
    
}

url = r'http://127.0.0.1:8000/whatsapp/' 

response = requests.post(url, json=data1) 

print(response)