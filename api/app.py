from flask import Flask, request, redirect, render_template, flash, Blueprint
app = Flask(__name__)
app.secret_key = 'development key'

#Blueprints
from blueprints.artist.artist import artist
from blueprints.recommended.recommended import recommended
from blueprints.recent.recent import recent

app.register_blueprint( artist, url_prefix='/artist' )
app.register_blueprint( recommended, url_prefix='/recommended' )
app.register_blueprint( recent, url_prefix='/recent' )

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)