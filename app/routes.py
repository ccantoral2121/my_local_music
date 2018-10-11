from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import NewArtistForm
from app import db
from app.models import Artist, Event, Venue, User
from app.forms import LoginForm
from app.forms import RegisterForm


@app.route('/')
@app.route('/index.html')
def index():

    return render_template('index.html', title='Home')


@app.route('/list_artists.html')
def list_artists():

    artists_list = Artist.query.all()
    return render_template('list_artists.html', list=artists_list, title='List of Artist')


@app.route( '/add.html', methods=['GET', 'POST'] )
def add_artist():

    form = NewArtistForm()
    if form.validate_on_submit():
        # Checks if artist is present in our database
        if Artist.query.filter_by(name=form.name.data).first():
            flash('Artist ' + form.name.data + ' is already in database')
            return render_template('add.html', title='Create New Artist', form=form)
        else:
            # if not present in our database then create new artist with info from form and add it to the database
            new_artist = Artist(name=form.name.data, hometown=form.hometown.data, description=form.description.data)
            db.session.add(new_artist)
            db.session.commit()
            flash('Artist ' + form.name.data + ' created and added to database')
            # return to the new artist page
            return artist(new_artist.name)
    return render_template('add.html', title='Create New Artist', form=form)


@app.route('/artist/<name>')
def artist(name):

    # checks if artist exist in database
    if Artist.query.filter_by(name=name).first():
        artist = Artist.query.filter_by(name=name).first()
        events = Event.query.filter_by(artistId=artist.id)
        return render_template('artist.html', artist=artist, title=artist.name, events=events)
    else:
        flash('Artist not in our database')
        return list_artists()


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("User is not available ")
        elif User.query.filter_by(email=form.email.data).first():
            flash("Email is already registered")
        else:
            new_user = User(username=form.username.data, email=form.email.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            index()
    return render_template('register.html', title='Register', form=form)


@app.route('/reset_db')
def reset_db():
    flash('resetting database: deleting old data and repopulating with dummy data')
    meta = db.metadata

    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
        db.session.commit()

    artisttest = [{"name": "Metallica",
                  "hometown": " Los Angeles, CA",
                  "description": "nice band"
                  },
                  {"name":"Korn",
                   "hometown":"Los Angeles,CA",
                    "description": "nice band"}
                 ]

    for a in artisttest:
        new_artist = Artist(name=a['name'], hometown=a['hometown'], description=a['description'])
        db.session.add(new_artist)
        db.session.commit()


    return render_template('index.html', title="Home")


if __name__ == '__main__':
    app.run()
