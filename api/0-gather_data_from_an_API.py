#!/usr/bin/python3
"""
Function to get employee information using the id
"""

import requests
import sys
if __name__ == '__main__':
    id = sys.argv[1]
    user = f'https://jsonplaceholder.typicode.com/users/{id}'
    user_data = requests.get(user)
    users = user_data.json()

    todo = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    todo_list = requests.get(todo)
    todos = todo_list.json()

    total_tasks = len(todos)
    completed_tasks = sum(1 for task in todos if task['completed'])

    print(f'Employee {users["name"]} is done with tasks({completed_tasks}/{total_tasks})')

    for item in todos:
        if item['completed']:
            print(f"\t{item['title']}")
