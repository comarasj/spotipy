from flask import Flask, request, redirect, render_template, flash
from flask_wtf import FlaskForm
from forms import ArtistPlaylistForm
from scripts import generator
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/playlist', methods=['POST'])
def playlist():
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
        
        return render_template('playlist.html', name=name, playlist_url=playlist_url)
    else:
        pass

if __name__ == '__main__':
    app.run(host='192.168.200.194', port='5000', debug=True)