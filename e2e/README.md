first step download the project 

```shell
$git clone https://github.com/ZhuSiyuan/todo-list
```

you must already start the backend and frontend server before e2e test

next step you need get in /e2e/ to do:

```shell
$npm install
$npm test
```

Tests include adding, modifying, and removing tasks
The test will automatically control the browser and you will see the following output

```shell
> todo-e2e@1.0.0 test E:\todo-list-demo\todo-list-demo\e2e
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
