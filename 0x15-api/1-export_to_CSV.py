#!/usr/bin/python3
"""  extend your Python script to export data in the CSV format """

import csv
import requests
from sys import argv


def write_to_csv(user_id, username, completed, title):
    """Writes the formatted data to a CSV file"""
    with open('USER_ID.csv', mode='a', newline='') as csvfile:
        csvwriter = csv.writer(
                csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csvwriter.writerow([str(user_id), username, str(completed), title])


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = int(argv[1])
    users = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos/"

    main_name = requests.get(users).json()
    todos_resp = requests.get(todos).json()

    if main_name is None:
        print(f"User with ID {user_id} not found.")
        exit(1)

    for todo in todos_resp:
        if user_id == todo.get('userId'):
            completed = todo.get('completed')
            title = todo.get('title')
            user_name = main_name.get('username')
            completed = todo.get('completed')
            write_to_csv(user_id, user_name, completed, title)
