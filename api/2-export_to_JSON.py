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


if __name__ == '__main__':
    id = sys.argv[1]
    employee_info(id)

