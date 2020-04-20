
'''
@author: zhusiyuan@stu.xjtu.edu.cn
@create date: 2020/4/20
@description: Backend's main method, start the app.
'''

from controller import app

if __name__ == '__main__':
    app.run(port=8080, debug=False)