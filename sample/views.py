import os
import krakenex
from django.shortcuts import render
from binance.client import Client

kraken = krakenex.API(key=os.environ['KRAKEN_API_KEY'], secret=os.environ['KRAKEN_API_SECRET'])
binance = Client(os.environ['BINANCE_API_KEY'], os.environ['BINANCE_API_SECRET'])

print(os.environ)

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

    return render(request, 'app/index.html', {
        'kraken_balance_info': kraken_balance_info.items(),
        'bitrex_balance_info': bitrex_balance_info
    })
