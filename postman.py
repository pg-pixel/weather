import requests 

data = {
    'Body':'Jaipur',
    'From':'whatsapp:+919986123781'
}
data1 =r"SmsMessageSid=SMf19af864a1fbceccdd85d3a4c3c700e5&NumMedia=0&ProfileName=Priyansh&SmsSid=SMf19af864a1fbceccdd85d3a4c3c700e5&WaId=919929712371&SmsStatus=received&Body=Hsjsms&To=whatsapp%3A%2B14155238886&NumSegments=1&ReferralNumMedia=0&MessageSid=SMf19af864a1fbceccdd85d3a4c3c700e5&AccountSid=AC323b81a3008306dbd52a171c5628727a&From=whatsapp%3A%2B919986123781&ApiVersion=2010-04-01"

url = r'http://127.0.0.1:8000/whatsapp/' 

response = requests.post(url, data=data1, headers={"Content-Type": "text/plain"}) 

print(response)