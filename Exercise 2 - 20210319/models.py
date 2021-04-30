from ws import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.String(160))
    description = db.Column(db.String(255))
    done = db.Column(db.String(10))

    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        return '<TaskModel %r>' % (self.id, self.title)