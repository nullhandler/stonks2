import requests
from mytoken import CTOKEN
import utils
import glob


def get_data(inst):
    url = utils.get_data_url(inst, '2020-11-30', '2020-12-30')
    response = requests.get(
        url,
        headers={
            "X-Kite-Version": "3",
            "Authorization": f"enctoken {CTOKEN}"
        },
    )
    return response.json()['data']['candles']


def get_data_if(i_name):
    if len(glob.glob(f'data/{i_name}.json')) == 0:
        i = utils.get_token([i_name], CTOKEN)
        utils.save_data(f'data/{i_name}.json', get_data(i[0]))



#inst1, inst2 = utils.get_token(["NIFTY20DEC13400PE", "NIFTY20DEC13400CE"], mytoken)
# nifty = utils.get_token(["NIFTY+50"], CTOKEN, "NSE")
#
# utils.save_data('data/nifty.json', get_data(nifty[0]))

