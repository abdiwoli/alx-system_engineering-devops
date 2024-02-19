#!/usr/bin/python3
""" module documentation """
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data['username']

    if not user_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if not todos_data:
        print(f"No TODOs found for {employee_name}.")
        return
    tasks = [task for task in todos_data]
    export_to_csv(employee_id, username, tasks)


def export_to_csv(user_id, user_name, completed_tasks):
    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for task in completed_tasks:
            writer.writerow({'USER_ID': str(user_id), 'USERNAME': user_name,
                             'TASK_COMPLETED_STATUS': task['completed'],
                             'TASK_TITLE': task['title']})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        get_employee_todo_progress(int(sys.argv[1]))
