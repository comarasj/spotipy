from flask import Flask, request, redirect, render_template, flash, Blueprint
app = Flask(__name__)
app.secret_key = 'development key'

#Blueprints
from artist.artist import artist
from recommended.recommended import recommended

app.register_blueprint(artist, url_prefix='/artist')
app.register_blueprint(recommended, url_prefix='/recommended')

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='192.168.200.194', port='5000', debug=True)