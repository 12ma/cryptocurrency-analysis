# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def home(request):
    import requests
    import json
    # Grab crypto price 
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,XLM,ADA,USDT,MIOTA,TRX&tsyms=INR,USD")
    price=json.loads(price_request.content)
    # Grab crypto news
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)
    return render(request,'home.html',{'api':api, 'price':price})
