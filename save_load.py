import json
data = "tasks.json"
def save_tasks(tasks):
    with open(data, "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():  
    try:
        with open (data, "r") as file:
            load_tasks = json.load(file)
            return load_tasks
    except FileNotFoundError:
        return[]
       