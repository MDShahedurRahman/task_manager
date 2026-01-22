from task_loader import load_tasks, save_tasks
from task_manager import add_task
from task_analyzer import count_by_status
from report import summary_report, print_report


def main():
    tasks = load_tasks()
    tasks = add_task(
        tasks,
        "Finish project",
        "Complete Python task manager",
        "2026-02-01",
        "HIGH"
    )
    save_tasks(tasks)

    counts = count_by_status(tasks)
    report = summary_report(tasks, counts)


if __name__ == "__main__":
    main()
