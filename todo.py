import json
import datetime
tasks = []
def add_task():
    task1 = input("Enter task name: ")
    task2 = input("Enter priority: ")
    task3 = input("Enter due_time: ")
    new_task = {
        "task": task1,
        "priority": task2,
        "due_date": task3,
        "completed": False
        }
    tasks.append(new_task)
    print("task successfully added")

def view_task():
    if not tasks :
        print("No tasks found.")
        return
    for index, task in enumerate(tasks):
        print(f"{index}. {task['task']} | Priority: {task['priority']} | Due: {task['due_date']}")
        if task["completed"] is True:
            print("COMPLETED")
        else:
            print("PENDING")

def complete_task():
    if not tasks:
        print("No task to complete")
        return
    view_task()
    show = int(input("Enter the number of the task to complete: "))
    tasks[show]["completed"] = True
    print("Task successfully completed")

def delete_task():
    if not tasks:
        print("No task to delete")
        return
    view_task()
    show = int(input("Enter the number of task to delete: "))
    tasks.pop(show)
    print("Task successfully deleted")

def edit_task():
    if not tasks:
        print("No task to edit: ")
        return
    view_task()
    show = int(input("Enter the number of the to edit: "))
    task1_new = input("Enter new task name")
    task2_new = input("Enter new priority")
    task3_new = input("Enter new due_time")
    tasks[show]["task"] = task1_new
    tasks[show]["priority"] = task2_new
    tasks[show]["due_date"] = task3_new
    print("successfully edited")
    
def filter_task ():
    if not tasks:
        print("No tasks found")
        return
    filter_choice = input("Filter by (1. pending, 2. Completed): ")
    if filter_choice == "1":
        tasks["completed"] is False
    elif filter_choice == "2":
        tasks["completed"] is True
    for index, task in enumerate(tasks):
        print(f"{index}. {task['task']} | Priority: {task['priority']} | Due: {task['due_date']}" )


    



def main ():
    while True:
        print("""
            1. Add task
            2. View tasks
            3. Complete task
            4. Edit task
            5. Delete task
            6. Filter tasks
            7. Exit
       """ )
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
           filter_task()
        elif choice == '7':
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again.")
        
if __name__ == "__main__": main()        
        
