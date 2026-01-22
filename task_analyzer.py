from utils import validate_date


def filter_by_status(tasks, status):
    return [t for t in tasks if t["status"] == status]
