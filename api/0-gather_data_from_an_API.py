#!/usr/bin/python3

import requests
import sys

def employee_info(id):
    # get user data
    user = f'https://jsonplaceholder.typicode.com/users/{id}'
    user_data = requests.get(user)
    users = user_data.json()

    # get todos
    todo = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    todo_list = requests.get(todo)
    todos = todo_list.json()

    # calculate todos
    total_tasks = len(todos)
    completed_tasks = sum(1 for task in todos if task['completed'])

    # display response
    print(f'Employee {users["name"]} is done with tasks({completed_tasks}/{total_tasks})')

    # display title of the tasks completed
    for item in todos:
        if item['completed']:
            print(f"\t{item['title']}")


if __name__ == '__main__':
    id = sys.argv[1]
    employee_info(id)

