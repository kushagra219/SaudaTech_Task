import requests
from django.shortcuts import render, redirect
import json
from django.conf import settings
  
def tradeListView(request):
    API_ENDPOINT = "https://api.sauda.co/suvidha/allCompletedOffers"
    # data to be sent to api 
    API_KEY = "ORfbGjdg9IK4rC5IRmG48kptPkuQb5af"
    data = {
                'apiKey': API_KEY
           } 
    # sending post request and saving response as response object 
    response = requests.post(url=API_ENDPOINT, data=data) 
    json_data = json.loads(response.text)  
    return render(request, "trade_list.html", context={"data":json_data})
