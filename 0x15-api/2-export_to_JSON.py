#!/usr/bin/python3
"""A python script that returns information about an
employees TODO list progress.
"""
import csv
import json
import requests
import sys


def get_todo_info():
    """A function that gets the todo information for a particular user id"""
    user_id = sys.argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                     .format(user_id))
    user = json.loads(r.text)
    user_name = user[0].get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(user_id))
    todos = json.loads(r.text)

    d = {f"{user_id}": []}
    for i in todos:
        d[f"{user_id}"].append({"username": user_name, "task": i["title"],
                                "completed": i["completed"]})

    with open('{}.json'.format(user_id),
              'w', newline='', encoding='utf-8') as fp:
        json.dump(d, fp, ensure_ascii=False, separators=(',', ':'))


if __name__ == "__main__":
    get_todo_info()
