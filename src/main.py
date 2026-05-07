from src.task_manager import add_task, list_tasks, complete_task


def main():
    print("Task Manager")
    tasks = list_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks):
        status = "✔" if task.get("done") else "✗"
        print(f"{index + 1}. [{status}] {task.get('title')}")


if __name__ == "__main__":
    main()
