import krakenex
from django.shortcuts import render
from django.conf import settings
from pprint import pprint # remove
from binance.client import Client

kraken = krakenex.API(key=settings.KRAKEN_API_KEY, secret=settings.KRAKEN_API_SECRET)
binance = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)

def index(request):
    kraken_balance_info = kraken.query_private('Balance')

    bitrex_balance_info = binance.get_account()

    pprint(bitrex_balance_info)

    return render(request, 'app/index.html', {
        'kraken_balance_info': kraken_balance_info,
        'bitrex_balance_info': bitrex_balance_info
    })
