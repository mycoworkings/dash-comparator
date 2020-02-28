from utils.dates_manipulation import substract_dates_from_today


def define_user_activity(last_click_date, page_views: int) -> dict:

    if last_click_date and page_views:
        dates_diff = substract_dates_from_today(last_click_date)
        return {
            "zombie": True if dates_diff >= 90 else False,
            "moderately_active": True if 30 <= dates_diff < 90 and page_views > 1 else False,
            "active": True if 15 <= dates_diff < 30 and page_views > 1 else False,
            "super_active": True if dates_diff < 15 and page_views > 1 else False
        }

    else:
        return {
            "zombie": None,
            "moderately_active": None,
            "active": None,
            "super_active": None
        }
