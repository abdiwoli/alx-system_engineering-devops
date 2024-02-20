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

    with open('{}.csv'.format(user_id),
              'w', newline='', encoding='utf-8') as fp:
        taskwriter = csv.writer(fp, quoting=csv.QUOTE_ALL)
        for task in todos:
            taskwriter.writerow(["{}".format(user_id),
                                 "{}".format(user_name),
                                 "{}".format(task.get('completed')),
                                 "{}".format(task.get('title'))])


if __name__ == "__main__":
    get_todo_info()
