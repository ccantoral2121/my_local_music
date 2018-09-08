from flask import render_template
from app import app



@app.route('/')
@app.route('/index.html')
def index():

    return render_template('index.html')

@app.route('/list_artists.html')
def list_artists():


    list = ['Eminem','Kaney West','MGK']

    return render_template('list_artists.html',list=list)

@app.route('/create.html')
def create_new_artist():

    return render_template('create.html')

@app.route('/mockup.html')
def mockup():
    return render_template('mockup.html')

if __name__ == '__main__':
    app.run()
