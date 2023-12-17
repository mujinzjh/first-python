from flask import jsonify

class HttpCode(object):
    ok = 200
    un_auth_error = 401
    params_error = 400
    server_server = 500


def http_result(code, message, data, result):
    return jsonify({"code": code, "message": message, "result": result, "data": data or {}})

def http_success(message="success", result=False, data=None):
    return http_result(code=HttpCode.ok, message=message, data=data, result=result)