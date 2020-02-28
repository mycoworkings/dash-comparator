from utils.mkt_email_stats_data import get_dict_values_from_key
from utils.dates_manipulation import unix_date_conversion
from utils.user_activity import define_user_activity


def get_contacts_data(contacts: dict, fields: list) -> dict:
    contacts_data = dict()

    for field in fields:
        if field in contacts.get("properties"):
            contacts_data[field] = get_dict_values_from_key(contacts.get("properties"), key1=field, key2="value")
        else:
            contacts_data[field] = None

    return contacts_data


def manipulate_contacts_data(contacts_data: dict) -> dict:
    contacts_data["date_birth_pet"] = unix_date_conversion(contacts_data["date_birth_pet"])
    user_activity = define_user_activity(contacts_data["hs_email_last_click_date"],
                                         int(contacts_data["hs_analytics_num_page_views"]))

    contacts_data["createdate"] = unix_date_conversion(contacts_data["createdate"])
    contacts_data["hs_email_last_click_date"] = unix_date_conversion(contacts_data["hs_email_last_click_date"])

    return {**contacts_data, **user_activity}