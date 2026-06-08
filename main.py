import os
import json

file_path = "data.json"
tasks = {}
task_id_counter = 1

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as f:
        tasks = json.load(f)

    tasks = {int(k): v for k, v in tasks.items()}

    if tasks:
        task_id_counter = max(tasks.keys()) + 1

else:
    tasks = {}

def main_menu():

    while True:

        print("---TASK MANAGEMENT APP---")
        print("1. Add task")
        print("2. View task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. View Stats")
        print("6. Save & Exit")

        choice = int(input("Enter your choice(1-7) : "))

        if choice == 1:
            add_task()

        elif choice == 2:
            view_tasks()

        elif choice == 3:
            mark_task()

        elif choice == 4:
            del_task()

        elif choice == 5:
            view_stats()

        elif choice == 6:
            save_exit()

        else:
            print("Invalid Choice")


def add_task():
    global task_id_counter

    print("--- ADD TASK ---")

    task_name = input("Enter task: ")
    status = input("Enter status (pending/completed) : ")

    tasks[task_id_counter] = {
        "task": task_name,
        "status": status
    }

    print(f"Task added successfully with ID {task_id_counter}")

    task_id_counter += 1

    input("Press Enter to return to menu : ")


def view_tasks():

    print("--- ALL TASKS ---")

    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for id, data in tasks.items():
            print(f"ID: {id}")
            print(f"Task: {data['task']}")
            print(f"Status: {data['status']}")
            print("-------------------")

    input("Press Enter to return to menu : ")
    
    
def mark_task():
    
    print("--- ALL TASKS ---")

    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for id, data in tasks.items():
            print(f"ID: {id}")
            print(f"Task: {data['task']}")
            print(f"Status: {data['status']}")
            print("-------------------")
    
    ask_id = int(input("Enter ID : "))
    
    if(ask_id in tasks):
        tasks[ask_id]["status"] = "completed"
        print("Task marked as completed successfully.")
        
    else:
        print("ID not found!")
        

def del_task():
    
    print("--- ALL TASKS ---")

    if len(tasks) == 0:
        print("No tasks found.")
        
    else:
        for id, data in tasks.items():
            print(f"ID: {id}")
            print(f"Task: {data['task']}")
            print(f"Status: {data['status']}")
            print("-------------------")
            
    ask2_id = int(input("Enter ID : "))
    
    if ask2_id in tasks:
        del tasks[ask2_id]
        print("Task deleted successfully!")
    else:
        print("ID not found!")
        
        
def view_stats():
    total = len(tasks)
    completed = 0
    pending = 0

    for task in tasks.values():
        if task["status"] == "completed":
            completed += 1
        else:
            pending += 1

    if total == 0:
        completion_rate = 0
    else:
        completion_rate = (completed / total) * 100

    print("--- TASK STATS ---")
    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    print(f"Completion Rate: {completion_rate:.2f}%")

    input("Press Enter to return to menu...")
    
    
def save_exit():
    with open(file_path, "w") as f:
        json.dump(tasks, f)

    print("Tasks saved successfully!")
    print("Exiting program...")
    exit()

main_menu()