from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import requests


# Create your views here.



class Homepage(ListView):
    
    
    def api(self):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q":"san francisco"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "617c887084mshc2fc6e3384e1d36p1bb283jsn058840ac0b53"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        result = response.json()
        print(result)
        return result
    
    def get(self, request):
        weather = self.api()
        temp = int(int(weather['main']['temp']) * 9/5 - 459.67)
        context = { 'city': "hello world", 'temp': temp  }
        
        return render(request, 'weather/index.html', context)

