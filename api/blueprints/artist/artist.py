from flask import Blueprint, render_template, abort, request
from flask_wtf import FlaskForm
from scripts import generator
import csv


artist = Blueprint('artist', __name__, template_folder='templates')

@artist.route('/')
def show():
    try:
        return render_template('artist.html', location='artist')
    except TemplateNotFound:
        abort(404)

@artist.route('/playlist', methods =['POST'])
def submit_here():
    if request.method == 'POST':
        artists = []
        name = request.form['playlistname']
        artist1 = request.form['artist1']
        artist2 = request.form['artist2']
        artist3 = request.form['artist3']
        artist4 = request.form['artist4']
        artist5 = request.form['artist5']
        artists.append(artist1)
        if artist2:
            artists.append(artist2)
        if artist3:
            artists.append(artist3)
        if artist4:
            artists.append(artist4)
        if artist5:
            artists.append(artist5)
        playlist_url = generator.main(name, artists)
        
        row = [ name, playlist_url ]
        with open( 'playlist.csv', 'a+', newline='' ) as fd:
            csv_writer = csv.writer( fd )
            csv_writer.writerow( row )
        
        return render_template( 'playlist.html', name=name, playlist_url=playlist_url )
    else:
        pass