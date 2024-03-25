#!/usr/bin/python3
"""Export data in the JSON format."""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    tasks = requests.get(url + "todos").json()

    todo_all_employees = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [{"username": username,
                       "task": task.get("title"),
                       "completed": task.get("completed")}
                      for task in tasks if task.get("userId") == user_id]
        todo_all_employees[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_all_employees, jsonfile)
