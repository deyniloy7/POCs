from flask import jsonify


def makeJsonResponse(success: object, message: object, errorCode: object, data: object) -> object:
    responseBody = {
        "success": success,
        "message": message,
        "error_code": errorCode,
        "data": data
    }

    return jsonify(responseBody)
