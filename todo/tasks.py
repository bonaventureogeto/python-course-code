def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added: {task}")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("Your Tasks: ")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def complete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to mark as done: "))
    if 1 <= num <= len(tasks):
        tasks[num - 1] += " -> COMPLETE"
        print("Task marked as done!")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(f"DELETED: {removed}")
    else:
        print("Invalid task number.")
