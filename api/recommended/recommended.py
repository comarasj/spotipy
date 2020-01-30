from flask import Blueprint, render_template, abort, request
from flask_wtf import FlaskForm

from scripts import generator

recommended = Blueprint('recommended', __name__, template_folder='templates')

@recommended.route('/')
def show():
    return 'Recommendation Page'