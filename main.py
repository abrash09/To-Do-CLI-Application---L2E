from todo import add_task
from todo import view_task
from todo import complete_task
from todo import edit_task
from todo import delete_task
from todo import filter_task
from save_load import save_tasks
from save_load import load_tasks

def main ():
    global tasks
    tasks = load_tasks()
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
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '2':
            view_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
           filter_task(tasks)
        elif choice == '7':
            save_tasks(tasks)
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again.")
        
if __name__ == "__main__": main()        
        