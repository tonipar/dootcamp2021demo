from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursename = db.Column(db.String(64), index=True, unique=True)
    courseholes = (db.Integer)
    
    def __repr__(self):
        return '<Course {}>'.format(self.coursename)

class Hole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holenum = db.Column(db.Integer, index=True)
    holepar = db.Column(db.Integer)
    holelength = db.Column(db.Integer)
    holecourse_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return '<Hole {}>'.format(self.holenum)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rounddate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    roundweather = db.Column(db.String(16))
    rounduser_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    roundcourse_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return '<Hole {}>'.format(self.date)

class Roundscore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hole = db.Column(db.Integer)
    score = db.Column(db.Integer)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'))