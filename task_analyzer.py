from utils import validate_date


def filter_by_status(tasks, status):
    return [t for t in tasks if t["status"] == status]


def filter_by_due_date(tasks, due_date):
    if not validate_date(due_date):
        return []
    return [t for t in tasks if t["due_date"] == due_date]
