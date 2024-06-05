#!/usr/bin/python3
"""Python script to export data in the CSV format."""

import requests
import sys
import csv


if __name__ == "__main__":

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(user_id)).json()
    todos_data = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user_data.get("username")
    csv_filename = "{}.csv".format(user_id)

    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow(
                [user_id, username, task.get("completed"), task.get("title")]
            )
