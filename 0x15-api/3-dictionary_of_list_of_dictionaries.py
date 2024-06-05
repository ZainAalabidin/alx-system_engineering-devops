#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(user_id)).json()
    todos_data = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user_data.get("username")

    all_tasks = {}
    for user in user_data:
        user_id = user["id"]
        username = user["username"]
        all_tasks[str(user_id)] = []

        for task in todos_data:
            task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            all_tasks[str(user_id)].append(task_info)

    json_filename = "todo_all_employees.json"

    with open(json_filename, mode="w") as file:
        json.dump(all_tasks, file)
