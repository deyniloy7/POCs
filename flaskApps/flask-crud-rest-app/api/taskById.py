from flask_restful import Resource
import logging as logger

class TaskById(Resource):

    def get(self, taskId):
        logger.debug("Inside get method of taskById")
        return {"message": "inside get method of taskById. taskId = {}".format(taskId)}, 200

    def post(self, taskId):
        logger.debug("Inside post method of taskById")
        return {"message": "inside post method of taskById. taskId = {}".format(taskId)}, 200

    def put(self, taskId):
        logger.debug("Inside put method of taskById")
        return {"message": "inside put method of taskById. taskId = {}".format(taskId)}, 200

    def delete(self, taskId):
        logger.debug("Inside delete method of taskById")
        return {"message": "inside delete method of taskById. taskId = {}".format(taskId)}, 200
