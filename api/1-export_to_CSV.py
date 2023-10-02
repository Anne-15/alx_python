#!/usr/bin/python3

import requests
import sys
import csv

def user_info(id):
    # get user data
    user = f'https://jsonplaceholder.typicode.com/users/{id}'
    user_data = requests.get(user)
    users = user_data.json()

    # get todos
    todo = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    todo_list = requests.get(todo)
    todos = todo_list.json()
    

    # exporting to a csv
    csv_file = f"{id}.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])
        for item in todos:
            writer.writerow([id, users['name'], str(item['completed']), item['title']])
    
    print(f"CSV file '{csv_file}' created successfully.")


if __name__ == '__main__':
    id = int(sys.argv[1])
    user_info(id)

