#!/usr/bin/python3
"""
Function to get employee information using the id
"""

import json
import requests
import sys

def employee_info():
    # get user data
    users_url = f'https://jsonplaceholder.typicode.com/users'
    user_data = requests.get(users_url)
    users = user_data.json()

    all_employees = {}

    for user in users:
        user_id = user['id']

        # fetch todos
        todo = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        todo_list = requests.get(todo)
        todos = todo_list.json()

        # exporting to a json
        user_info = [
                {
                    "username": user['username'],
                    "task": items['title'],
                    "completed": items['completed'],
                }

                for items in todos
            ]
        

        all_employees[user_id] = user_info
    
    json_file = "todo_all_employees.json"

    # write data to json file
    with open(json_file, 'w') as json_files:
        json.dump(all_employees, json_files)

    print(f"JSON file '{json_file}' created successfully.")


if __name__ == '__main__':
    employee_info()

