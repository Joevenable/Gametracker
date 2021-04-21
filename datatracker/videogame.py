from flask import Blueprint, render_template
from types import SimpleNamespace
#from datatracker.api import api
import requests, json

bp = Blueprint('searching', __name__)

@bp.route('/videogame', methods=['GET'])
def index():
        response = requests.get('https://api.dccresource.com/api/games')
        data = response.content
        return render_template('videogame/index.html', data=data)

        #print(response.content)
        #years = response.json()
        #print()
        #game = response.json()
        #print(game[0]['name'])

        #json_data = response.content
        #json_data_dict = json.loads(json_data)
        #print(json_data_dict('year'))
        #year = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
        #global_sales = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
       # for sales in global_sales:
                       ## if year[0] >= 2013:
                             #   print(sales.globalSales)
              #  else:
                      #  print("No sales this year")
        #for sale_year in year:






# video_game.py
# register a blueprint
# create one endpoint
# visit it, go from there