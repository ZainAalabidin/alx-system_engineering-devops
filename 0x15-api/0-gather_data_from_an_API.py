#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":

    user_id = int(sys.argv[1])

    # Base URLs for the API
    users_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    
    user_response = requests.get(users_url)

    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get(todos_url)

    todos_data = todos_response.json()

    completed_tasks = [todo for todo in todos_data if todo.get('completed')]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
