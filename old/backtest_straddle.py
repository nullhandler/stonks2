import json
from datetime import datetime, timedelta
import utils
from getData import get_data_if
from old.backtest import back_test


def backtest_straddle(main_file, b):
    buy_time = b
    main = json.load(open(main_file))
    for i_index in range(len(main)):
        i1 = main[i_index]
        date = datetime.strptime(i1[0].split('+')[0], "%Y-%m-%dT%H:%M:%S")
        if date == buy_time:
            strike_price = str(int(utils.get_nearest(i1[1], 50)))
            ce_name = f'NIFTY20DEC{strike_price}CE'
            pe_name = f'NIFTY20DEC{strike_price}PE'
            get_data_if(ce_name)
            get_data_if(pe_name)
            back_test(f'data/{ce_name}.json', f'data/{pe_name}.json', date, False)
            buy_time = buy_time + timedelta(days=utils.get_next_date_difference(main[i_index:], buy_time))


backtest_straddle("../data/nifty.json", datetime.strptime("2020-12-01T12:00:00", "%Y-%m-%dT%H:%M:%S"))