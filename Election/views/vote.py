from flask import Blueprint, render_template, make_response
from models import *

vote_page = Blueprint('vote_page', __name__, template_folder='templates', static_folder='static')

@vote_page.route('/')
def index():
    return render_template('views/vote/index.html')



@vote_page.route('status')
def status():
    return 'OK', 200
    