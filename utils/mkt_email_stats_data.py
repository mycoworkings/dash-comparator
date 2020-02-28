from datetime import datetime
from utils.verifiers import check_device_breakdown


def get_dict_values_from_key(email: dict, **kwargs):
    try:
        if kwargs.get("key2"):
            return email.get(kwargs.get("key1")).get(kwargs.get("key2"))
        else:
            return email.get(kwargs.get("key1"))
    except KeyError:
        print("Can't access or not existing value")


# get_email_id(email)
def get_email_id(email: dict):
    return get_dict_values_from_key(email, key1="id")


# get_email_counters_stats(email.get("stats"), key1="open")
def get_email_counters_stats(email: dict, **kwargs):
    return get_dict_values_from_key(email.get("counters"), key1=kwargs.get("key1"))


# get_email_device_data(email.get("stats"), key1="open_device_type", key2="mobile")
def get_email_device_data(email: dict, **kwargs):
    if check_device_breakdown(email):
        return get_dict_values_from_key(email.get("deviceBreakdown"), key1=kwargs.get("key1"), key2=kwargs.get("key2"))
    else:
        return None


def get_mkt_email_statistics(email_data: dict) -> dict:
    return {
        "ID": get_email_id(email_data),
        "SENT": get_email_counters_stats(email_data.get("stats"), key1="sent"),
        "OPEN": get_email_counters_stats(email_data.get("stats"), key1="open"),
        "DELIVERED": get_email_counters_stats(email_data.get("stats"), key1="delivered"),
        "BOUNCE": get_email_counters_stats(email_data.get("stats"), key1="bounce"),
        "UNSUBSCRIBED": get_email_counters_stats(email_data.get("stats"), key1="unsubscribed"),
        "CLICK": get_email_counters_stats(email_data.get("stats"), key1="click"),
        "SPAM_REPORT": get_email_counters_stats(email_data.get("stats"), key1="spam_report"),
        "PENDING": get_email_counters_stats(email_data.get("stats"), key1="pending"),
        "NOT_SENT": get_email_counters_stats(email_data.get("stats"), key1="not_sent"),
        "OPEN_COMPUTER": get_email_device_data(email_data.get("stats"), key1="open_device_type", key2="computer"),
        "OPEN_MOBILE": get_email_device_data(email_data.get("stats"), key1="open_device_type", key2="mobile"),
        "OPEN_UNKNOWN": get_email_device_data(email_data.get("stats"), key1="open_device_type", key2="unknown"),
        "CLICK_COMPUTER": get_email_device_data(email_data.get("stats"), key1="click_device_type", key2="computer"),
        "CLICK_MOBILE": get_email_device_data(email_data.get("stats"), key1="click_device_type", key2="mobile"),
        "CLICK_UNKNOWN": get_email_device_data(email_data.get("stats"), key1="click_device_type", key2="unknown"),
        "ACCESS_DATE_TIME": datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    }
