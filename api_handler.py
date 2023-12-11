from flask import jsonify, request

def handle_api_get_request(view_func):
    def wrapper(*args, **kwargs):
        params = request.args.to_dict()
        result = view_func(params, *args, **kwargs)
        return jsonify(result)
    return wrapper

def handle_api_post_request(view_func):
    def wrapper(*args, **kwargs):
        data = request.json
        result = view_func(data, *args, **kwargs)
        return jsonify(result)
    return wrapper