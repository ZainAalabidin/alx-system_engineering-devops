#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users").json()
    todos_data = requests.get(url + "todos").json()

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
