#!/usr/bin/python3
import json
import requests
import sys

emp_id = sys.argv[1]

# url_todos = 'https://jsonplaceholder.typicode.com/todos/{}'.format(emp_id)
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
    user_id = emp["userId"]
    user_status = emp["completed"]
    if int(user_id) == int(emp_id) and user_status:
        done_task += 1


emp_info = "Employee {} is done with tasks({}/20):".format(emp_name, done_task)

print(emp_info)


for emp in todos_dict:
    user_id = emp["userId"]
    user_status = emp["completed"]
    if int(user_id) == int(emp_id) and user_status:
        indented_output = "\t" + emp["title"]
        print(indented_output)
