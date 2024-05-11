#!/usr/bin/python3
"""0-gather_data_from_an_API """

from sys import argv
import requests


def get_name(users, employee_id) -> None:
    """
    Gets the names of the employee

    Arg:
        users (dict): The first argument
        employee_id (int): The second argument

    Return:
        None
    """

    for user in users:
        if user['id'] == employee_id:
            return user['name']


def get_employee_tasks(todos, employee_id):
    """
    Gets the employee's tasks details

    Arg:
        todos (dict): The first argument
        employee_id (int): The second argument

    Return:
        int: total_tasks
        int: completed tasks
        str: completed_task_titles
    """
    total_tasks = 0
    completed_tasks = 0
    completed_task_titles = []
    for todo in todos:
        if todo['userId'] == employee_id:
            total_tasks += 1
            if todo['completed'] is True:
                completed_tasks += 1
                completed_task_titles.append(todo['title'])

    return (total_tasks, completed_tasks, completed_task_titles)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    users_resp = requests.get(url_users)
    todos_resp = requests.get(url_todos)

    users = users_resp.json()
    todos = todos_resp.json()

    employee_name = get_name(users, employee_id)
    if employee_name is None:
        print(f"Employee with ID {employee_id} not found.")
        exit(1)

    all_tasks, complete_tasks, titles = get_employee_tasks(todos, employee_id)

    print(f"{employee_name} is done with task ({complete_tasks}/{all_tasks}):")
    for title in titles:
        print(f"\t{title}")
