from app import db
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    hometown = db.Column(db.String(64), index=True)
    description = db.Column(db.TEXT, index=True)
    #relationships with Event, ArtistToEvent table
    events = db.relationship('Event', backref='artist', lazy=True)
    artist = db.relationship('ArtistToEvent', backref='artist',lazy=True)

    def __repr__(self):
        return '<Artist {}>'.format(self.name)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    date = db.Column(db.String(15), index=True)
    #Foreing keys from Artist, Venue tables
    artistId = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venueId = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    #relationship to ArtistToEvent
    event = db.relationship('ArtistToEvent', backref='event',lazy=True)

    def __repr__(self):
        return '<Event {}>'.format(self.title)


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(100), index=True, nullable=False)
    events = db.relationship('Event', backref='venue', lazy=True)

    def __repr__(self):
        return '<Venue {}>'.format(self.name)

class ArtistToEvent(db.Model):
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), primary_key=True, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True, nullable=False)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.body)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
