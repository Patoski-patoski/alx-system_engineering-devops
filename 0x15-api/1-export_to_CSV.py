#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID, returns
    information about his/her TODO list progress
"""

import requests
from sys import argv


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
            print("\"{}\", \"{}\", \"{}\" \"{}\"):".format(
                user_id, main_name.get('username'), completed, title))
