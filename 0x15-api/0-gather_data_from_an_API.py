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

    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(user_id)).json()
    todos_data = requests.get(url + "todos", params={"userId": user_id}).json()
    employee_name = user_data.get("name")

    completed_tasks = [todo for todo in todos_data if todo.get("completed")]
    total_number_of_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
