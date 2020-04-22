
# todo-list 后端

### 运行环境：
- Python 3
- Flask
- pytest

### 安装：

1. 
```shell
pip install flask pytest
```

2. 到 [Google 应用商店](https://chrome.google.com/webstore/category/extensions) 安装 [Allow CORS: Access-Control-Allow-Origin](https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?hl=zh-CN)，并将 CORS 开关开启。
> 这一步是由于 React 与 Flask 交互时，fetch 出错：No Access-Control-Allow-Origin header is present on the requested resource。
> 
> 参考[【已解决】ReactJS中用fetch出错：No Access-Control-Allow-Origin header is present on the requested resource](https://www.crifan.com/reactjs_fetch_no_access_control_allow_origin_header_is_present_on_the_requested_resource/)，macOS 的 Chrome 浏览器默认禁止了跨域访问 CORS。
> 
> 因此需要手动关闭 Chrome 的 CORS，否则 Flask 后端只能与 Postman 交互，而无法与 React 正常交互。


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
