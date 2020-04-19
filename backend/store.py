
'''
@author: zhusiyuan@stu.xjtu.edu.cn
@create date: 2020/4/19
@description: Backend's store, reading and writing data from files.
'''

import json

FILE = './data.json'
def get_tasks():
    with open(FILE, 'r') as file:
        tasks = json.loads(file.read())
    return tasks

def set_tasks(tasks):
    with open(FILE, 'w') as file:
        file.write(json.dumps(tasks))