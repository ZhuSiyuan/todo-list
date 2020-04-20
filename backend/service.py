
'''
@author: zhusiyuan@stu.xjtu.edu.cn
@create date: 2020/4/19
@description: Backend's service, doing CRUD for tasks.
'''

from store import get_tasks, set_tasks

class TaskService:
    
    # 查找全部task
    @staticmethod
    def query_all():
        tasks = get_tasks()
        return tasks
    
    # 查找指定id的task
    @staticmethod
    def query_by_id(id):
        tasks = get_tasks()
        for item in tasks:
            if id == item['id']:
                return item
        return None

    # 插入task_insert到tasks
    @staticmethod
    def insert(task_insert):
        tasks = get_tasks()
        for item in tasks:
            if task_insert['id'] == item['id']:
                return False, 'Insert failed, database already exists "id=%s"' % task_insert['id']
        tasks.append(task_insert)
        set_tasks(tasks)
        return True, tasks
    
    # 更新task_update
    @staticmethod
    def update(task_update):
        tasks = get_tasks()
        for item in tasks:
            if task_update['id'] == item['id']:
                item['content'] = task_update['content']
                set_tasks(tasks)
                return True, tasks
        return False, 'Update failed, database do not exist "id=%s"' % task_update['id']

    # 删除指定id的task
    @staticmethod
    def delete_by_id(id):
        tasks = get_tasks()
        for item in tasks:
            if id == item['id']:
                tasks.remove(item)
                set_tasks(tasks)
                return True, tasks
        return False, 'Delete failed, database do not exist "id=%s"' % (id)
