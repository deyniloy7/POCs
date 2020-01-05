from flask_restful import Api
from app import flaskAppInstance
from .task import Task
from .taskById import TaskById

restServer = Api(flaskAppInstance)

restServer.add_resource(Task, "/api")
restServer.add_resource(TaskById, "/api/<string:taskId>")