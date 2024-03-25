#!/usr/bin/python3
"""using this REST API, for a given employee ID"""
import csv
import requests
import sys

if __name__ == "__main__":
    """Main Module"""
    id = int(sys.argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    name = user.json().get('name')
    username = user.json().get('username')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = 0
    tasks_done = 0
    for task in todos.json():
        if task.get('userId') == id:
            tasks += 1
            if task.get('completed'):
                tasks_done += 1

    print(f"Employee {name} is done with tasks({tasks_done}/{tasks}):")
    for task in todos.json():
        if task.get('userId') == id and task.get('completed'):
            title = task.get('title')
            print(f"\t {title}")

    csv_file = f"{id}.csv"
    with open(csv_file, mode='w') as f:
        writer = csv.writer(f, delimiter=",", quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == id:
                writer.writerow([id, username, str(task.get('completed')),
                                task.get('title')])
