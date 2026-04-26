tasks = []
task_id_counter = 1

def create_task(task_data):
    global task_id_counter

    task = {
        "id": task_id_counter,
        "title": task_data.title,
        "isCompleted": task_data.isCompleted
    }

    tasks.append(task)
    task_id_counter +=1
    return task

def get_task():
    return tasks

def get_task_by_id(task_id: int):
    return next((task for task in tasks if task["id"] == task_id), None)

def update_task(task_id: int, update_data):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = update_data.title
            task["isCompleted"] = update_data.isCompleted
            return task
    return None 

def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return True