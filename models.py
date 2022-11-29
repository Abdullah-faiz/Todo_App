from db import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    title = db.Column(db.String(200), nullable=True)

    def __init__(self, title, note):
        self.note = note
        self.title = title

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'note': self.note}


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'username': self.username}
