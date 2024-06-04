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

    user_id = int(sys.argv[1])

    # Base URLs for the API
    users_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    
    user_response = requests.get(users_url)

    user_data = user_response.json()
    user_name = user_data.get('name')

    todos_response = requests.get(todos_url)

    todos_data = todos_response.json()
    csv_filename = f"{user_id}.csv"

    tasks = []
    for task in todos_data:
        task_info = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_name
        }
        tasks.append(task_info)

    user_tasks = {str(user_id): tasks}
    json_filename = f"{user_id}.json"

    with open(json_filename, mode='w') as file:
        json.dump(user_tasks, file)
