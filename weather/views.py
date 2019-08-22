import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
     

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
    
        req = requests.get(url.format(city)).json()
    
        city_weather = {
            'city': city.name,
            'temperature' : ((req['main']['temp'])-32)//1.8,
            'description' : req['weather'][0]['description'],
            'icon' : req['weather'][0]['icon'],
            'humid' : req['main']['humidity'],

    }

        weather_data.append(city_weather)
    context = {'weather_data' : weather_data, 'form':form}
    

    return render(request, 'weather/weather.html', context)