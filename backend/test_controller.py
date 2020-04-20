
'''
@author: zhusiyuan@stu.xjtu.edu.cn
@create date: 2020/4/20
@description: Test controller.py.
'''

import pytest
from controller import app


class TestClass(object):

    def setup_class(self):
        # 测试开始时首先执行，准备工作
        app.config['TESTING'] = True
        self.app = app.test_client()

    def teardown_class(self):
        # 测试结束时执行，收尾工作，关闭资源
        pass

    def test_query_all(self):
        response = self.app.get('/api/tasks/')
        assert 200 == response.status_code

    def test_query_by_id(self):
        response = self.app.get('/api/tasks/1')
        assert 200 == response.status_code

        response = self.app.get('/api/tasks/1x')
        assert 403 == response.status_code

    def test_insert(self):
        raise NotImplementedError

    def test_update(self):
        raise NotImplementedError

    def test_delete_by_id(self):
        raise NotImplementedError


if __name__ =="__main__":
    pytest.main(['test_controller.py','-s'])
