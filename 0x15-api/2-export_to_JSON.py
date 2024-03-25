#!/usr/bin/python3
"""using this REST API, for a given employee ID"""
import requests
import json
import sys

if __name__ == "__main__":
    """Main Module"""
    id = int(sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    name = user.json().get('username')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = []
    for task in todos.json():
        if task.get('userId') == id:
            task_title = task.get('title')
            task_completed = task.get('completed')
            tasks.append({"task": task_title,
                          "completed": task_completed,
                          "username": name})
    json_file = f"{id}.json"
    with open(json_file, mode='w') as f:
        json.dump({str(id): tasks}, f)
