"""
this extra file has been made/created to avoid circular loop, leading to exception!
"""


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
