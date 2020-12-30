import requests
import mytoken as tk
import utils
mytoken = tk.TOKEN


def get_data(inst):
    url = utils.get_data_url(inst, '2020-11-30', '2020-12-30')
    response = requests.get(
        url,
        headers={
            "X-Kite-Version": "3",
            "Authorization": f"enctoken {mytoken}"
        },
    )
    return response.json()['data']['candles']


inst1, inst2 = utils.get_token(["NIFTY20DEC13400PE", "NIFTY20DEC13400CE"], mytoken)
print(inst1)
print(inst2)

utils.save_data('data/1.json', get_data(inst1))
utils.save_data('data/2.json', get_data(inst2))

