#!/usr/bin/python3
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if not user_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_name = user_data['name']
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if not todos_data:
        print(f"No TODOs found for {employee_name}.")
        return
    completed_tasks = [task for task in todos_data if task['completed']]
    lnt = '{len(todos_data)}'
    lnc = 'len(completed_tasks)'
    print(f"Employee {employee_name} is done with tasks {lnc}/{lnt}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
