#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID, returns
    information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    users = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos/"

    employee_name = requests.get(users).json().get('name')
    todos_resp = requests.get(todos).json()

    if employee_name is None:
        print(f"Employee with ID {employee_id} not found.")
        exit(1)

    total_tasks = 0
    completed_tasks = 0
    completed_task_titles = []

    for todo in todos_resp:
        if employee_id == todo.get('userId'):
            total_tasks += 1
            if todo.get('completed') is True:
                completed_tasks += 1
                completed_task_titles.append(todo.get('title'))

    print("{} is done with task ({}/{}):".format(
        employee_name, completed_tasks, total_tasks))

    for title in completed_task_titles:
        print(f"\t{title}")
