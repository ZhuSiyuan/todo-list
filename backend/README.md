
# todo-list 后端

### 运行环境：
- Python 3
- Flask
- pytest

### 安装：
```shell
pip install flask pytest
```

### 使用：
```shell
python main.py
```

然后，在浏览器端访问：
[http://127.0.0.1:8080/api/tasks/](http://127.0.0.1:8080/api/tasks/)

应显示：

```
[
  {
    "content": "Restful API Demo", 
    "createdTime": "2019-05-15T00:00:00Z", 
    "id": 1
  }
]
```

### 测试：
```shell
python test_store.py
python test_service.py
python test_controller.py
```

应显示：

```shell
$ python test_store.py 
..
2 passed in 0.01 seconds

$ python test_service.py 
.....
5 passed in 0.01 seconds

$ python test_controller.py 
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /path/to/todo-list/backend, inifile: 
collected 5 items 

test_controller.py .....

=========================== 5 passed in 0.03 seconds ===========================
```