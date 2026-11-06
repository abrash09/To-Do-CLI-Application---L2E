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
            print("coming soon")
        elif choice == '4':
            print("coming soon")
        elif choice == '5':
            print("coming soon")
        elif choice == '6':
            print("coming soon")
        elif choice == '7':
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again.")
        
if __name__ == "__main__": main()        
        
