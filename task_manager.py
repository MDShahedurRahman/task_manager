from task import Task
from utils import generate_task_id, validate_date


def add_task(tasks, title, description, due_date, priority):
    if not validate_date(due_date):
        raise ValueError("Invalid date format")

    task_id = generate_task_id(tasks)
    task = Task(task_id, title, description, due_date, "PENDING", priority)
    tasks.append(task.to_dict())
    return tasks


def update_task_status(tasks, task_id, status):
    for t in tasks:
        if t["task_id"] == task_id:
            t["status"] = status
    return tasks


def update_task_priority(tasks, task_id, priority):
    for t in tasks:
        if t["task_id"] == task_id:
            t["priority"] = priority
    return tasks
