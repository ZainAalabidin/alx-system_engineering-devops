#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests

if __name__ == "__main__":

    # Base URL of the REST API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data and todos data from the API
    user_data = requests.get(url + "users").json()
    todos_data = requests.get(url + "todos").json()

    # Dictionary to store all tasks, indexed by user ID
    all_tasks = {}

    # Loop through each user
    for user in user_data:
        # Extract user ID and username
        user_id = user["id"]
        username = user["username"]

        # List to store tasks for this user
        user_tasks = []

        # Loop through all tasks
        for task in todos_data:
            # Check if the task belongs to the current user
            if task["userId"] == user_id:
                # If yes, extract task information and add to user_tasks list
                task_info = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username,
                }
                user_tasks.append(task_info)

        # Store the user_tasks list in the all_tasks dictionary, indexed by user ID
        all_tasks[str(user_id)] = user_tasks

    # Export the all_tasks dictionary to a JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode="w") as file:
        json.dump(all_tasks, file)
