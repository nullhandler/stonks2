import json
from datetime import datetime, timedelta
import utils


def back_test(file1, file2, b, check_daily):
    buy_time = b
    inst1 = json.load(open(file1))
    inst2 = json.load(open(file2))
    buy_price = 0
    target = 0
    losses = 0
    profits = 0
    stop_loss = 0
    for i_index in range(len(inst1)):
        i1 = inst1[i_index]
        i2 = inst2[i_index]
        date = datetime.strptime(i1[0].split('+')[0], "%Y-%m-%dT%H:%M:%S")
        if buy_price == 0 and date == buy_time:
            buy_price = i1[1] + i2[1]
            target = buy_price + buy_price * 0.005
            stop_loss = buy_price - buy_price * 0.01
        if buy_price != 0:
            # Order Executed
            if i1[1] + i2[1] > target:
                print(f"Profit Bought at: {buy_price}, Sold at: {round(target,2)}, Buy:{date.strftime('%Y-%m-%d %I:%M')}")
                profits += 1
                if check_daily:
                    buy_time = buy_time + timedelta(days=utils.get_next_date_difference(inst1[i_index:], buy_time))
                    buy_price = 0
                else:
                    break
            if i1[1] + i2[1] < stop_loss:
                print(f"Loss Bought at: {buy_price}, Sold at: {round(stop_loss,2)}, Date:{date.strftime('%Y-%m-%d %I:%M')}")
                losses += 1
                if check_daily:
                    buy_time = buy_time + timedelta(days=utils.get_next_date_difference(inst1[i_index:], buy_time))
                    buy_price = 0
                else:
                    break
    #print(f'Profits: {profits} Losses: {losses}')


#back_test('data/1.json', 'data/2.json', datetime.strptime("2020-12-01T13:00:00", "%Y-%m-%dT%H:%M:%S"), True)


