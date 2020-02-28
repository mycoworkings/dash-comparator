from utils.mkt_email_stats_data import get_dict_values_from_key


def get_pages_fields(page: dict) -> dict:
    page_data = dict()
    fields = ['ab', 'absolute_url', 'analytics_page_id', 'analytics_page_type', 'archived', 'current_state',
              'currently_published', 'html_title', 'label']

    for field in fields:
        if field in page:
            page_data[field] = get_dict_values_from_key(page, key1=field)
        else:
            page_data[field] = None

    return page_data

