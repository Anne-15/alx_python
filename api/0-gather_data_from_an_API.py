#!/usr/bin/python3
"""
Returning value of todo items per user
"""
import requests
import sys

if __name__=="__main__":
    user_id = sys.argv[1]

    # getting user
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url)
    user_data = user.json()

    # getting todos
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    todos = requests.get(todo_url)
    todos_data = todos.json()

    # all tasks
    total_tasks = len(todos_data)

    count = 0
    # completed tasks
    for todo in todos_data:
        if(todo['completed'] == True):
            count += 1

    print(f'Employee {user_data["name"]} is done with tasks({count}/{total_tasks}):')
    
    for tasks in todos_data:
        if(tasks['completed']):
            print(f"\t{tasks['title']}")
    
    
            