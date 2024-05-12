#!/usr/bin/python3
"""  Python script to export data in the CSV format. """

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = int(argv[1])
    users = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos/"

    main_name = requests.get(users).json().get('username')
    todos_resp = requests.get(todos).json()

    for todo in todos_resp:

        with open(f'{argv[1]}.csv', 'a', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            completed = todo.get('completed')
            title = todo.get('title')
            completed = todo.get('completed')
            csvwriter.writerow([user_id, main_name, completed, title])
