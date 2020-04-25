from flask import Blueprint, render_template, abort, request
from flask_wtf import FlaskForm
from scripts import generator
import csv


recent = Blueprint( 'recent', __name__, template_folder='templates' )

@recent.route( '/' )
def show_recent_playlists():
    try:
        playlists_name = []
        playlists_url = []

        with open( 'playlist.csv', 'r' ) as fd:
            reader = csv.reader( fd, delimiter=',' )
            for i, line in enumerate( reader ):
                playlists_name.append( line[ 0 ] )
                playlists_url.append( line[ 1 ] )
        return render_template( 'recent.html', len=len(playlists_url), playlists_url=playlists_url, playlists_name=playlists_name )
    except TemplateNotFound:
        abort( 404 )