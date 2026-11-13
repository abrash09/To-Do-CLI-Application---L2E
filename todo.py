import datetime
def add_task(task_list):
    task1 = input("Enter task name: ")
    task2 = input("Enter priority: ")
    task3 = input("Enter due_time: ")
    new_task = {
        "task": task1,
        "priority": task2,
        "due_date": task3,
        "completed": False
        }
    task_list.append(new_task)
    print("task successfully added")

def view_task(task_list):
    if not task_list :
        print("No tasks found.")
        return
    for index, task in enumerate(task_list):
        print(f"{index}. {task['task']} | Priority: {task['priority']} | Due: {task['due_date']}")
        if task["completed"] is True:
            print("COMPLETED")
        else:
            print("PENDING")

def complete_task(task_list):
    if not task_list:
        print("No task to complete")
        return
    view_task(task_list)
    show = int(input("Enter the number of the task to complete: "))
    task_list[show]["completed"] = True
    print("Task successfully completed")

def delete_task(task_list):
    if not task_list:
        print("No task to delete")
        return
    view_task(task_list)
    show = int(input("Enter the number of task to delete: "))
    task_list.pop(show)
    print("Task successfully deleted")

def edit_task(task_list):
    if not task_list:
        print("No task to edit: ")
        return
    view_task()
    show = int(input("Enter the number of the to edit: "))
    task1_new = input("Enter new task name")
    task2_new = input("Enter new priority")
    task3_new = input("Enter new due_time")
    task_list[show]["task"] = task1_new
    task_list[show]["priority"] = task2_new
    task_list[show]["due_date"] = task3_new
    print("successfully edited")
    
def filter_task (task_list):
    if not task_list:
        print("No tasks found")
        return
    filter_choice = input("Filter by (1. pending, 2. Completed): ")
    for index, task in enumerate(task_list):
        if filter_choice == "1":
            if task["completed"] is False:
                print(f"{index}. {task['task']} | Priority: {task['priority']} | Due: {task['due_date']}" )
        elif filter_choice == "2":
            if task["completed"] is True:
                print(f"{index}. {task['task']} | Priority: {task['priority']} | Due: {task['due_date']}" )
    
       
        
