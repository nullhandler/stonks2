from getData import *
import utils
from api.kite import get_historical_data

# print(utils.get_token(["NIFTY21APR14000PE"]))
print(get_historical_data("779521"))