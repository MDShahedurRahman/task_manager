def summary_report(tasks, status_counts):
    return {
        "total_tasks": len(tasks),
        "status_breakdown": status_counts
    }
