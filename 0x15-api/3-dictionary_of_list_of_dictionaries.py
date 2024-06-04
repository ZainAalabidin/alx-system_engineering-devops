#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
import sys
import json


if __name__ == "__main__":

    # Base URLs for the API
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    
    users_response = requests.get(users_url)

    users_data = users_response.json()

    todos_response = requests.get(todos_url)

    todos_data = todos_response.json()

    all_tasks = {}
    for user in users_data:
        user_id = user['id']
        username = user['username']
        all_tasks[str(user_id)] = []

        for task in todos_data:
            task_info = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            all_tasks[str(user_id)].append(task_info)

    json_filename = "todo_all_employees.json"

    with open(json_filename, mode='w') as file:
        json.dump(all_tasks, file)
