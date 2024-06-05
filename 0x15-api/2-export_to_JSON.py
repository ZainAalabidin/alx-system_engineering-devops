#!/usr/bin/python3
"""export data in the JSON format."""
import requests
import sys
import json


if __name__ == "__main__":

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(user_id)).json()
    todos_data = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user_data.get("username")

    tasks = []
    for task in todos_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        tasks.append(task_info)

    user_tasks = {str(user_id): tasks}
    json_filename = "{}.json".format(user_id)

    with open(json_filename, mode="w") as file:
        json.dump(user_tasks, file)
