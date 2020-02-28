import os


def check_email_state(state) -> bool:
    return True if "DRAFT" not in state else False


def check_device_breakdown(email: dict) -> bool:
    return True if email.get("deviceBreakdown") else False


# Check if the input path exists or not
def check_existing_path(path: str) -> bool:
    return True if os.path.exists(path) else False


# Check if path has the slash "/" at the end of the string, if not it's added
def check_path_structure(path: str) -> str:
    return path if "/" in path[-1] else f'{path}/'
