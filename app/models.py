from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login



# Contains models for database tables. SQLAlchemy will convert these to proper tables for database.

# Loads given users Id for Flask-Login to keep track logged users.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Model for User table. Usermixin will add is_authenticated, is_active, is_anonymous, get_id() properties 
# for the user model.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    rounds = db.relationship('Round', backref='user', lazy='dynamic')

    # creates hashed password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # check if password is correct
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursename = db.Column(db.String(64), index=True, unique=True)
    courseholes = db.Column(db.Integer)
    courselocation = db.Column(db.String(64))
    rounds = db.relationship('Round', backref='course', lazy='dynamic')
    holes = db.relationship('Hole', backref='course', lazy='dynamic')
    
    def __repr__(self):
        return '<Course {}>'.format(self.coursename)



class Hole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holenum = db.Column(db.Integer, index=True)
    holepar = db.Column(db.Integer)
    holelength = db.Column(db.Integer)
    holecourse_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    db.UniqueConstraint('holenum', 'holecourse_id', name='coursehole')

    def __repr__(self):
        return '<Hole {}>'.format(self.holenum)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rounddate = db.Column(db.DateTime, default=datetime.utcnow)
    roundweather = db.Column(db.String(16))
    rounduser_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    roundcourse_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    roundscores = db.relationship('Roundscore', backref='round', lazy='dynamic')

    def __repr__(self):
        return '<Hole {}>'.format(self.date)

class Roundscore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hole = db.Column(db.Integer)
    score = db.Column(db.Integer)
    ob = db.Column(db.Boolean)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'))
    db.UniqueConstraint('hole', 'round_id', name='roundhole')