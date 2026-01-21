from datetime import datetime
from config import DATE_FORMAT


def validate_date(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False


def generate_task_id(tasks):
    if not tasks:
        return 1
    return max(t["task_id"] for t in tasks) + 1
