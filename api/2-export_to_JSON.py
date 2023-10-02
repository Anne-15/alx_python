#!/usr/bin/python3
"""
Function to get employee information using the id
"""

import json
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

    # exporting to a json
    json_file = f"{id}.json"
    
    user_info = {
        f"{id}": [
            {
                "task": items['title'],
                "completed": items['completed'],
                "username": users['name'],
            }

            for items in todos
        ]
    }

    # write data to json file
    with open(json_file, 'w', encoding='utf-8') as json_files:
        json.dump(user_info, json_files, indent=2)

    print(f"JSON file '{json_file}' created successfully.")


if __name__ == '__main__':
    id = sys.argv[1]
    employee_info(id)

