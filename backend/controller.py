
'''
@author: zhusiyuan@stu.xjtu.edu.cn
@create date: 2020/4/20
@description: Backend's controller, handling requests corresponding to the predefined RESTful API.
'''

import json
from flask import Flask, request, jsonify

from service import TaskService

JSON_AS_ASCII = False
app = Flask(__name__)


# index page
@app.route('/', methods=['GET'])
def index():
    return 'hello world', 200


# 返回所有Todo任务
@app.route('/api/tasks/', methods=['GET'])
def query_all():
    tasks = TaskService.query_all()
    return jsonify(tasks), 200


# 返回一个指定ID的Todo任务
@app.route('/api/tasks/<id>', methods=['GET'])
def query_by_id(id=None):
    try:
        id = int(id)
    except:
        return '"id" must be a integer', 403

    task = TaskService.query_by_id(id)
    if task is None:
        return 'Not found, no "id=%s" item in database' % (id), 404
    else:
        return jsonify(task)


# 创建一个新的Todo任务
@app.route('/api/tasks/', methods=['POST'])
def insert():
    task_insert = str(request.get_data(), encoding='utf-8')
    try:
        task_insert = json.loads(task_insert)
    except:
        return 'Please check the validity of the data', 403

    state, msg = TaskService.insert(task_insert)
    if state is False:
        return msg, 403
    else:
        return jsonify(msg), 200


# 更新一个新的Todo任务
@app.route('/api/tasks/', methods=['PUT'])
def update():
    task_update = str(request.get_data(), encoding='utf-8')
    try:
        task_update = json.loads(task_update)
    except:
        return 'Please check the validity of the data', 403

    state, msg = TaskService.update(task_update)
    if state is False:
        return msg, 403
    else:
        return jsonify(msg), 200


# 删除一个Todo任务
@app.route('/api/tasks/<id>', methods=['DELETE'])
def delete_by_id(id=None):
    try:
        id = int(id)
    except:
        return '"id" must be a integer', 403

    state, msg = TaskService.delete_by_id(id)
    if state is False:
        return msg, 404
    else:
        return jsonify(msg), 200


if __name__ == '__main__':
    app.run(debug=True)