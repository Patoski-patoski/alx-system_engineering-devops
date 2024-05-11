#!/usr/bin/python3
import requests
from sys import argv

url_users = f"https://jsonplaceholder.typicode.com/users"
url_todo = f"https://jsonplaceholder.typicode.com/todos"

employee_id = int(argv[1])
TASKS_DONE = 0
TOTAL_NUM_TASKS = 0
TASK_TITLE = ""

users_resp = requests.get(url=url_users)
todos_resp = requests.get(url=url_todo)

users = users_resp.json()
todos = todos_resp.json()

save_id = ""
employee_name = ""
for user in users:
    if user['id'] == employee_id:
        employee_name = user['name']
        break

for todo in todos:
    if todo['userId'] == employee_id:
        TOTAL_NUM_TASKS += 1
        if todo['completed'] is True:
            TASKS_DONE += 1


print(f"{employee_name} is done with task ({TASKS_DONE}/{TOTAL_NUM_TASKS}):")

for todo in todos:
    if todo['completed'] is True and todo['userId'] is employee_id:
        TASK_TITLE = todo['title']
        print(f"\t{TASK_TITLE}")
