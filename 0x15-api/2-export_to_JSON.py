#!/usr/bin/python3
"""  Python script to export data in the JSON format """

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    if len(argv) != 2:
        print(f"Usage: python {argv[0]}  {argv[1]}")
        exit(1)

    user_id = argv[1]
    users = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos/"

    main_name = requests.get(users).json().get('username')
    todos_resp = requests.get(todos).json()

    with open(f"{user_id}.json", mode='w', encoding='utf-8') as json_file:
        json.dump({user_id: [{
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': main_name
            } for todo in todos_resp]}, json_file)
