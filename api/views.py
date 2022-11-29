from flask import Blueprint, request, jsonify
from flask import json, make_response
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from cryptography.fernet import Fernet

from api.helper_functions import add_todo, update_todo, delete_todo, get_todo, add_user
from models import User

api_blueprint = Blueprint('api_blueprint', __name__)
api = Api(api_blueprint)

parser = reqparse.RequestParser()

auth = HTTPBasicAuth()

key = Fernet.generate_key()
f = Fernet(key)
print(key)


@auth.verify_password
def verify_password(username, password):
    return check_password_hash(User.query.filter(User.email == username).first().password, password)


class UserViewSet(Resource):

    def post(self):
        try:
            if hasattr(request, 'data') and request.data not in [None, b'', " ", {}]:
                data = json.loads(request.data)
                email = data.get("email", None)
                username = data.get("username", None)
                password = data.get("password", None)
                if email and username:
                    user = add_user(email, username, password)
                    user_dict = user.serialize()
                    user_dict = json.dumps(user_dict)
                    user_dict = user_dict.encode('utf')
                    return make_response(f.encrypt(user_dict))
                else:
                    return make_response(jsonify({"success": False, "error": "email and username required!"}), 400)
            else:
                return make_response(jsonify({"success": False, "error": "invalid data!"}), 400)
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 500)


class TodoViewSet(Resource):

    @auth.login_required
    def post(self):
        try:
            if hasattr(request, 'data') and request.data not in [None, b'', " ", {}]:
                data = json.loads(request.data)
                note = data.get("note", None)
                title = data.get("title", None)
                if note:
                    todo = add_todo(note, title)
                    todo_dict = todo.serialize()
                    todo_dict = json.dumps(todo_dict)
                    todo_dict = todo_dict.encode('utf')
                    return make_response(f.encrypt(todo_dict))
                else:
                    return make_response(jsonify({"success": False, "error": "note is required!"}), 400)
            else:
                return make_response(jsonify({"success": False, "error": "invalid data!"}), 400)
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 500)

    @auth.login_required
    def put(self):
        try:
            todo_id = request.args.get("todo_id", None)
            if todo_id:
                if hasattr(request, 'data') and request.data not in [None, b'', " ", {}]:
                    data = json.loads(request.data)
                    note = data.get("note", None)
                    title = data.get("title", None)
                    if note:
                        todo = update_todo(todo_id, note, title)
                        todo_dict = todo.serialize()
                        todo_dict = json.dumps(todo_dict)
                        todo_dict = todo_dict.encode('utf')
                        return make_response(f.encrypt(todo_dict))
                    else:
                        return make_response(jsonify({"success": False, "error": "note is required!"}), 400)
                else:
                    return make_response(jsonify({"success": False, "error": "invalid data!"}), 400)
            else:
                return make_response(jsonify({"success": False, "error": "todo_id is required!"}), 400)
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 500)

    @auth.login_required
    def get(self):
        try:
            todo_id = request.args.get("todo_id", None)
            todo = get_todo(todo_id)
            todo_dict = {'data': [e.serialize() for e in todo]}
            todo_dict = json.dumps(todo_dict)
            todo_dict = todo_dict.encode('utf')
            return make_response(f.encrypt(todo_dict))
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 500)

    @auth.login_required
    def delete(self):
        try:
            todo_id = request.args.get("todo_id", None)
            if todo_id:
                delete = delete_todo(todo_id)
                if delete:
                    return make_response(jsonify({"success": True, "response": "successfully deleted!"}), 200)
            else:
                return make_response(jsonify({"success": False, "error": "todo_id is required!"}), 400)
        except Exception as e:
            return make_response(jsonify({"success": False, "error": str(e)}), 500)


api.add_resource(TodoViewSet, '/todo/')
api.add_resource(UserViewSet, '/user/')
