
'''
@author: zhusiyuan@stu.xjtu.edu.cn
@create date: 2020/4/19
@description: Test service.py.
'''

import pytest
from service import TaskService


def test_query_all():
    tasks = TaskService.query_all()
    assert 1 == len(tasks)
    assert 'Restful API Demo' == tasks[0]['content']


def test_query_by_id():
    task = TaskService.query_by_id(1)
    assert 'Restful API Demo' == task['content']


def test_insert():
    task = {
        "content": "test insert", 
        "createdTime": "2020-04-19T00:00:00Z", 
        "id": 2
    }
    TaskService.insert(task)
    tasks =TaskService.query_all()
    assert 2 == len(tasks)
    assert 'test insert' == tasks[1]['content']


def test_update():
    task = {
        "content": "test update", 
        "createdTime": "2020-04-19T00:00:00Z", 
        "id": 2
    }
    TaskService.update(task)
    tasks =TaskService.query_all()
    assert 2 == len(tasks)
    assert 'test update' == tasks[1]['content']


def test_delete_by_id():
    state, msg = TaskService.delete_by_id(2)
    assert True == state
    tasks =TaskService.query_all()
    assert 1 == len(tasks)


if __name__ == '__main__':
    pytest.main(['-q', 'test_service.py'])