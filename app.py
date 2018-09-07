from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():

    return render_template('index.html')

@app.route('/artists.html')
def list_artists():

    return render_template('artists.html')

@app.route('/create.html')
def create_new_artist():

    return render_template('create.html')

if __name__ == '__main__':
    app.run()
