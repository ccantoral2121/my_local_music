from flask import render_template
from app import app
from app.forms import NewArtistForm



@app.route('/')
@app.route('/index.html')
def index():

    return render_template('index.html',title='Home')

@app.route('/list_artists.html')
def list_artists():


    list = ['Eminem','Kaney West','MGK']


    return render_template('list_artists.html',list=list,title='List of Artist')


@app.route('/add.html')
def add_artist():

    form = NewArtistForm()
    return render_template('add.html', title='Create New Artist', form=form)


@app.route('/artist.html')
def artist_page():
    artist = {'name': 'Eminem',
              'hometown': 'St. Joseph, Missouri, U.S.',
              'description': 'Marshall Bruce Mathers III (born October 17, 1972), known professionally as Eminem (often stylized as EMINƎM) is an American rapper, songwriter, record producer, record executive, and actor.',
              'events': ['Saturday 15 September 2018, England','Sunday 16 September 2018, Munich']
              }

    return render_template('artist.html', artist=artist)

if __name__ == '__main__':
    app.run()
