
## todo-list e2e测试

### 安装：

```shell
npm install
```

### 使用：

```shell
npm test
```

工作台应输出：

```shell
> todo-e2e@1.0.0 test \path\to\todo-list\e2e
> mocha test/bootstrap.js --recursive test --timeout 10000

  Todo List
      √ should have correct title
    add task
      √ should create new task and add to the end (882ms)
    edit task
      √ should update task (423ms)
    delete the new task
      √ should delete the new task in the end of the list (544ms)
    4 passing (12s)
```
