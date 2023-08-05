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
import csv
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
    emp_name = name_dict["username"]

    # Employee todos
    todos_dict = json.loads(todos_data)
    csv_file_name = "{}.csv".format(emp_id)
    data_csv = []
    for emp in todos_dict:
        user_id = emp.get("userId")
        user_status = emp.get("completed")
        user_todos = emp.get("title")
        if int(user_id) == int(emp_id):
            save_to_csv = [user_id, emp_name, user_status, user_todos]
            formatted_save_to_csv = [f'"{item}"' for item in save_to_csv]

            data_csv.append(formatted_save_to_csv)

    with open(csv_file_name, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerows(data_csv)
