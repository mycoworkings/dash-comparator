from utils.mkt_email_stats_data import get_dict_values_from_key


def get_forms_fields(form_name: str, fields: dict) -> dict:
    return {
        "NAME": form_name,
        "FORM_NAME": get_dict_values_from_key(fields, key1="name"),
        "LABEL": get_dict_values_from_key(fields, key1="label"),
        "GROUP_NAME": get_dict_values_from_key(fields, key1="groupName"),
        "REQUIRED": get_dict_values_from_key(fields, key1="required"),
    }