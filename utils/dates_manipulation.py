from datetime import datetime, date
import pandas as pd


def unix_date_conversion(ux_date):
    if ux_date:
        return datetime.fromtimestamp(int(ux_date) / 1000).date()
    else:
        return None


def substract_dates_from_today(start_date):
    return pd.date_range(unix_date_conversion(start_date), date.today()).shape[0]
