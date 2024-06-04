#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
import sys
import csv


if __name__ == "__main__":

    user_id = int(sys.argv[1])

    # Base URLs for the API
    users_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_response = requests.get(users_url)

    user_data = user_response.json()
    user_name = user_data.get("name")

    todos_response = requests.get(todos_url)

    todos_data = todos_response.json()
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow(
                [user_id, user_name, task.get("completed"), task.get("title")]
            )
