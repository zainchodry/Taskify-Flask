from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    tasks = db.relationship('Task', backref = 'owner', lazy = True)



class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    due_date = db.Column(db.Date, nullable = True)
    status = db.Column(db.String(50), default = 'Pending')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))