
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
    raise NotImplementedError


def test_update():
    raise NotImplementedError


def test_delete_by_id():
    raise NotImplementedError


if __name__ == '__main__':
    pytest.main(['-q', 'test_service.py'])