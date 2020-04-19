
'''
@author: zhusiyuan@stu.xjtu.edu.cn
@create date: 2020/4/19
@description: Test store.py.
'''

import pytest
from store import get_tasks, set_tasks


def test_get_tasks():
    tasks = get_tasks()
    assert len(tasks) == 1
    assert 'Restful API Demo' == tasks[0]['content']


def test_set_tasks():
    tasks = get_tasks()
    tasks[0]['content'] = 'test set_tasks'
    set_tasks(tasks)
    tasks = get_tasks()
    assert 'test set_tasks' == tasks[0]['content']

    tasks[0]['content'] = 'Restful API Demo'
    set_tasks(tasks)


if __name__ == '__main__':
    pytest.main(['-q', 'test_store.py'])