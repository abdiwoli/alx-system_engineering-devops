#!/usr/bin/python3
"""A python script that returns information about an
employees TODO list progress.
"""
import requests
import json


def get_todo_info():
    """A function that gets the todo information for a particular user id"""
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users = json.loads(r.text)

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = json.loads(r.text)
    d = {}
    did = {}

    for sid in users:
        user_id = sid["id"]
        d[user_id] = []
        did[user_id] = sid["username"]

    for i in todos:
        user_id = i["userId"]
        d[user_id].append({
            "username": did[user_id],
            "task": i["title"],
            "completed": i["completed"]
        })

    with open('todo_all_employees.json', 'w', newline='',
              encoding='utf-8') as fp:
        json.dump(d, fp, ensure_ascii=False, separators=(',', ':'))


if __name__ == "__main__":
    get_todo_info()
