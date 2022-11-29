from werkzeug.security import generate_password_hash

from db import db
from models import Todo, User


def add_user(email, username, password):
    user_obj = User.query.filter(User.email == email).first()
    if user_obj:
        return user_obj
    user_obj = User(email=email, username=username, password=generate_password_hash(password))
    db.session.add(user_obj)
    db.session.commit()
    return user_obj


def add_todo(note, title=None):
    todo_obj = Todo(note=note, title=title)
    db.session.add(todo_obj)
    db.session.commit()
    return todo_obj


def delete_todo(todo_id):
    Todo.query.filter(Todo.id == todo_id).delete()
    db.session.commit()
    return True


def update_todo(todo_id, note, title):
    todo_obj = Todo.query.filter(Todo.id == todo_id).first()
    todo_obj.note = note
    todo_obj.title = title
    db.session.commit()
    return todo_obj


def get_todo(todo_id=None):
    if todo_id:
        todo_objs = Todo.query.filter(Todo.id == todo_id)
    else:
        todo_objs = Todo.query.all()
    return todo_objs
