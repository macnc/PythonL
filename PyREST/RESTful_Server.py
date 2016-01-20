#!~/anaconda2/bin/python
# _*_coding: utf-8

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# 需要鉴权使用的用户信息API
class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')

# 处理任务列表逻辑的API
class TaskListAPI(Resource):
    def get(self):
        pass

    # def put(self):
    #     pass

    def post(self):
        pass

# 处理单项任务逻辑的API
class TaskAPI(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint = 'tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint = 'tasks')