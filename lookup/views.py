###############
import requests
import json
from twilio.rest import Client
from enum  import Enum
################
from django.shortcuts import render, HttpResponse 
from django.views.decorators.csrf import csrf_exempt
################
from weather.settings import WEATHER_KEY as key
from weather.settings import TWILIO_ACCOUNT_SID as account_sid 
from weather.settings import TWILIO_AUTH_TOKEN as auth_token
################

class AQI_Index(Enum):
    _1 = 'Good' 
    _2 = 'Fair'
    _3 = 'Moderate'
    _4 = 'Poor' 
    _5 = 'very Poor'

class Application_logic:

    @staticmethod
    def get_city_latitude_longitude(city):
        latitude_longitude_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},IN&limit=5&appid={key}'
        
        latitude_longitude_response = requests.get(latitude_longitude_url).json()
        lat = latitude_longitude_response[0]['lat'] 
        lon = latitude_longitude_response[0]['lon'] 
        
        return lat, lon, city
    
    @staticmethod
    def get_aqi(latitude, longitude):
        aqi_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={key}'
        aqi_response = requests.get(aqi_url).json()
        
        context = {'AQI':aqi_response['list'][0]['main']['aqi'],
                   'Components': aqi_response['list'][0]['components'],
                   } 
        
        return context 
    
    @staticmethod
    def solution(city):
        latitude, longitude, city = Application_logic.get_city_latitude_longitude(city) 
        
        context = Application_logic.get_aqi(latitude, longitude)
        context['City'] = city 
        state = AQI_Index[f"_{str(context['AQI'])}"].value
        context['AQI'] = state
        
        return context
    
    @staticmethod
    def send_whatsapp_msg(to_number, message_dictionary):
        
        client = Client(account_sid, auth_token) 
        if message_dictionary:
            message = f"Your city is {message_dictionary['City']}. " \
                      f"Current AQI is: {message_dictionary['AQI']}. " 
        else:
            message = f"Welcome to PG's Weather App. Kindly type <city name> for your city information." \
                      f" Note: Only Indian cities supported so far. Please type your city name only. "
                  
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'{message}',
            to=f'whatsapp:{to_number}'
            )
        
        
def get_weather_details(request):
    
    if request.POST:
        if 'City' in request.POST:
            city = request.POST['City']
        else:
            city = 'Kota' # default value
            
        context = Application_logic.solution(city)
        
        return render(request, 'weather.html', context)
    
    else:
        context = {'Components':{}, }
        return render(request, 'weather.html', context)
   
@csrf_exempt 
def twilio_getweather_details(request):
    if request.method == 'POST':
        payload = json.loads(request.body) 
        
        city = payload.get('Body', '') 
        _from = list(payload.get('From', '').split(':'))[1]
        
        context = Application_logic.solution(city) 
        
        Application_logic.send_whatsapp_msg(_from, context)
        
        return HttpResponse(status=202)
        
        
    
    