import json, requests
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from types import SimpleNamespace
import urllib.request

bp = Blueprint('videogame', __name__)


@bp.route('/videogame', methods=['GET'])
def index():


        response = requests.get('https://api.dccresource.com/api/games')
        data = json.loads(response.content)
        #goal : Get all unique platforms
        unique_platofrms = {}
        game_data = json.loads(response.content, object_hook=lambda g: SimpleNamespace(**g))

        for game in game_data:
                game_platform = game.platform
                if game.year is not None and game.year > 2012:
                        if game_platform not in unique_platofrms:
                                unique_platofrms[game_platform] = game.globalSales
                        else:
                                unique_platofrms[game_platform] += game.globalSales


                # check if this game has a platform we haven't seen before
                # if platform exists in unique platforms, skip it
                # else add it to unique platforms

        # make a dictionary with platforms as keys
        # python turn list into dictionary keys

        global_sales_list = []
        for key in unique_platofrms:
                global_sales_list.append((unique_platofrms[key],key))


        global_sales_list = sorted(global_sales_list, key=lambda x: -x[0])



        labels = []
        values = []
        for game_platform in global_sales_list:
                values.append(game_platform[0])
                labels.append(game_platform[1])
        return render_template("videogame/index.html", labels=labels, values=values)

        # which key in the dictionary matches this game's platform?
        # add total sales to that key's value
        # python change values in dictonary



        return render_template('videogame/index.html')
        #for item in data:
                #if item.year  > 2013:
                        #print(item.name.name)

# class Search:
#         def __init__(self):
#                 self.__init__ == True
#
#         def searchByName(game_data, search):
#                 name_results = []
#                 if search is not '':
#                         for game in game_data:
#                                 if search in game.name:
#                                                 name_results.append(game)
#
#                         return name_results
#                 else:
#                         return name_results, 0

        # video_game.py
        # register a blueprint
        # create one endpoint
        # visit it, go from there









        #print(response.content)
        #years = response.json()
        #print()
        #game = response.json()
        #print(game[0]['name'])

        #json_data = response.content
        #json_data_dict = json.loads(json_data)
        #print(json_data_dict('year'))

        # years = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
        # platforms = json.loads(response.content, object_hook=lambda p: SimpleNamespace(**p))


        # years = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
        # for yearly in years:
        #         if yearly.year is not None:
        #                 if yearly.year > 2013:
        #                         print(yearly.platform)
        #
        #
        # global_sales = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
        # for sales in global_sales:
        #        print(sales.globalSales)
              #else:
                      #  print("No sales this year")
        #for sale_year in year:




# @bp.route('/videogame/publisher', methods =['GET', 'POST'])
# def publishers():
#         response = requests.get('https://api.dccresource.com/api/games')
#         games = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
#
#         gameplatforms = []
#         for game in games:
#                 platform = game.platform
#             if platform not in gameplatforms:
#                     gameplatforms.append(platform)
#
#         if request.method == 'POST':
#                 console_selected = request.form.get('consoles')
#             if console_selected is not None:
#             return render_template('videogame/publisher.html', console_selected = console_selected, platforms = gameplatforms, publishers =publishers)

