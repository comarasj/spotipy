from flask_wtf import Form
from wtforms import TextField, SubmitField, RadioField, validators

class ArtistPlaylistForm(Form):
    playlist_name = TextField("Name of Playlist", [validators.Required("Please enter a name for the Playlist")])
    artist1 = TextField("Artist 1", [validators.Required("Please enter an Artist")])
    artist2 = TextField("Artist 2")
    artist3 = TextField("Artist 3")
    artist4 = TextField("Artist 4")
    artist5 = TextField("Artist 5")
    length = RadioField('Playlist Length', choices = [('S','short'),('L','Long')])

