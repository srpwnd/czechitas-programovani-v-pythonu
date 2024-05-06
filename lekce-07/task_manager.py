import datetime


class Task:
    def __init__(self, description):
        self.description = description
        self.timestamp = datetime.datetime.now()


tasks = {}
id_counter = 0


def add_task(description):
    global id_counter
    task_id = id_counter
    tasks[task_id] = Task(description)
    id_counter += 1


def remove_task(task_id):
    if task_id in tasks:
        tasks.pop(task_id)


def show_tasks():
    if not tasks:
        print("Nothing to show")
    for id, task in tasks.items():
        print(f"Task {id} created at {task.timestamp}: {task.description}")


def main():
    while True:
        command = input("Insert command add, remove, or show: ")
        if command == "add":
            desc = input("Write task description: ")
            add_task(desc)
        elif command == "remove":
            task_id = int(input("Write task id to delete: "))
            remove_task(task_id)
        elif command == "show":
            show_tasks()
        else:
            print("Wrong command")


if __name__ == "__main__":
    main()
