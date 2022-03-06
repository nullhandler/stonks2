from api.common_kite import get
from api import urls
import datetime


def get_historical_data(instrument, from_date=None, to_date=None, time_frame="15minute"):
    """
    10 minute
    15 minute
    """
    return get(
        urls.historical_url.format(token=instrument, from_date=from_date or get_past_30_date(), to_date=to_date or get_current_date(), timeframe=time_frame)).json()


def get_current_date():
    return str(datetime.date.today())


def get_past_30_date():
    return str(datetime.date.today() - datetime.timedelta(days=30))
