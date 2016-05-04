# #!~/anaconda2/bin/python
# # _*_coding: utf-8

from flask import Flask
from flask_restful import Api, Resource, abort, marshal
from flask_restful import reqparse
from passlib.apps import custom_app_context as pwd_context
import sqlalchemy as db
from app import auth, api, tasks, task_fields


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


# 需要鉴权使用的用户信息API
class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')

# 处理任务列表逻辑的API
class TaskListAPI(Resource):

    decorators = [auth.login_required]

    def __int__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True,
                                   help = 'no task title provided', location = 'json')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(TaskListAPI, self).__init__()

    def get(self):
        pass

    # def put(self):
    #     pass

    def post(self):
        pass



# 处理单项任务逻辑的API
class TaskAPI(Resource):

    decorators = [auth.login_required]

    def __int__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskAPI, self).__init__()


    def get(self):
        pass

    def put(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                task[k] = v

        return {'task': marshal(task, task_fields)}

    def delete(self):
        pass

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint = 'tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint = 'tasks')
