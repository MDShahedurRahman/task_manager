from utils import validate_date


def filter_by_status(tasks, status):
    return [t for t in tasks if t["status"] == status]


def filter_by_due_date(tasks, due_date):
    return [t for t in tasks if t["due_date"] == due_date]
