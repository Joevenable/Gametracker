from flask import Blueprint, render_template
from types import SimpleNamespace
#from datatracker.api import api
import requests, json

bp = Blueprint('searching', __name__)

@bp.route('/videogame', methods=['GET'])
def index():
        response = requests.get('https://api.dccresource.com/api/games')
        print(response.content)
        game = response.json()
        print(game[0]['name'])






# video_game.py
# register a blueprint
# create one endpoint
# visit it, go from there