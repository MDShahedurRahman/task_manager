from task_loader import load_tasks, save_tasks
from task_manager import add_task
from task_analyzer import count_by_status
from report import summary_report, print_report


def main():
    tasks = load_tasks()


if __name__ == "__main__":
    main()
