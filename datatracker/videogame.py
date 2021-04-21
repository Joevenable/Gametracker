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

        global_Sales = json.laods(response.content, object_hook=lambda d: SimpleNamespace(**d))
        for sales in global_Sales:
                print(sales.globalSales)

        return render_template('videogame/index.html')




# video_game.py
# register a blueprint
# create one endpoint
# visit it, go from there