import requests
import json
from datetime import datetime
from mytoken import CTOKEN


def get_data_url(i_token, from_date, to_date, timeframe='15minute'):
    """
    timeframe: minute, 10minute, 15minute
    """
    return f'https://kite.zerodha.com/oms/instruments/historical/{i_token}/{timeframe}?user_id=IJ0147&oi=1&from={from_date}&to={to_date}'


def save_data(name, data):
    json.dump(data, open(name, 'w'))


def get_next_date_difference(tickers, today_date):
    for ticker in tickers:
        date = datetime.strptime(ticker[0].split('+')[0], "%Y-%m-%dT%H:%M:%S")
        if date.day != today_date.day:
            return (date - today_date).days + 1 # i have no clue why we are adding 1
    return 0


def get_token(names, exchange="NSE"):
    params = ""
    for name in names:
        params += f'i={exchange}:{name}&'
    url = 'https://api.kite.trade/quote/ltp?'
    response = requests.get(
        url,
        params=params,
        headers={
            "X-Kite-Version": "3",
            "Authorization": f"enctoken {CTOKEN}"
        },
    )
    print(response.json())
    return [i_token['instrument_token'] for i_token in response.json()['data'].values()]


def get_nearest(n, m):
    n1 = n % m
    n2 = m - n1
    if n1 > n2:
        return n + m - n1
    else:
        return n - n1
