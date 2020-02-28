from utils.mkt_email_stats_data import get_dict_values_from_key


def get_email_data(email: dict) -> dict:
    fields = ['ab', 'currentlyPublished', 'emailType', 'id', 'name', 'subject']
    email_data = dict()

    for field in fields:
        if field in email:
            email_data[field] = get_dict_values_from_key(email, key1=field)
        else:
            email_data[field] = None

    return email_data