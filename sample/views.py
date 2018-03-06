import krakenex
from django.shortcuts import render
from django.conf import settings
from binance.client import Client
from pprint import pprint # remove

kraken = krakenex.API(key=settings.KRAKEN_API_KEY, secret=settings.KRAKEN_API_SECRET)
binance = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)

def index(request):
    kraken_balance_info = kraken.query_private('Balance')
    bitrex_balance_info = binance.get_account()

    if 'result' in kraken_balance_info:
        kraken_balance_info = kraken_balance_info['result']
    else:
        kraken_balance_info = {}

    if 'balances' in bitrex_balance_info:
        bitrex_balance_info = bitrex_balance_info['balances']
    else:
        bitrex_balance_info = {}

    # For real circumstances I would call the exchanges only after loading the template page with JS

    pprint(bitrex_balance_info)

    return render(request, 'app/index.html', {
        'kraken_balance_info': kraken_balance_info.items(),
        'bitrex_balance_info': bitrex_balance_info
    })
