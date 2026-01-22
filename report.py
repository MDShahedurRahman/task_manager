def summary_report(tasks, status_counts):
    return {
        "total_tasks": len(tasks),
        "status_breakdown": status_counts
    }


def print_report(report):
    print("Task Summary Report")
    print("-------------------")
    print(f"Total Tasks: {report['total_tasks']}")
    for status, count in report["status_breakdown"].items():
        print(f"{status}: {count}")
