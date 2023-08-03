#!/usr/bin/python3
"""This script gathers data from an API based on the employee ID provided.

It uses the 'json', 'requests', and 'sys' modules to interact with the API
and retrieve data.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>

The script takes one argument - the employee ID -
and fetches the user information and
the todos for the given employee ID from the 'jsonplaceholder' API.

API URLs:
    url_todos:   'https://jsonplaceholder.typicode.com/todos'
    url_user:    'https://jsonplaceholder.typicode.com/users/<employee_id>'

The output shows the employee name and the list of completed tasks
for the given employee.

Example:
    ./0-gather_data_from_an_API.py 2
"""

import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)

    response_1 = requests.get(url_user)
    response_2 = requests.get(url_todos)

    name_data = response_1.text
    todos_data = response_2.text

    # Employee username
    name_dict = json.loads(name_data)
    emp_name = name_dict["name"]

    # Employee todos
    todos_dict = json.loads(todos_data)
    done_task = 0

    for emp in todos_dict:
        user_id = emp.get("userId")
        user_status = emp.get("completed")
        if int(user_id) == int(emp_id) and user_status:
            done_task += 1

    emp_info = "Employee {} is done with tasks({}/20):".format(
        emp_name, done_task)

    print(emp_info)

    for emp in todos_dict:
        user_id = emp.get("userId")
        user_status = emp.get("completed")
        if int(user_id) == int(emp_id) and user_status:
            indented_output = "\t" + emp["title"]
            print("\t {}".format(emp["title"]))
