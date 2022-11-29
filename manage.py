from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from db import db
from app import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    manager.run()

