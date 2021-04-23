import labels as labels
from Tools.scripts.make_ctype import values
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import json, requests
from types import SimpleNamespace
import urllib.request

bp = Blueprint('videogame', __name__)


@bp.route('/videogame', methods=['GET'])
def index():
    # response = requests.get('https://api.dccresource.com/api/games')
    # data = json.loads(response.content)

    # for item in data:
    # if item.year  > 2013:
    # print(item.name.name)

    # print(data)

    # dictname['listkeyvariable']['year']

    # print(response.content)
    # years = response.json()
    # print()
    # game = response.json()
    # print(game[0]['name'])

    # json_data = response.content
    # json_data_dict = json.loads(json_data)
    # print(json_data_dict('year'))

    # years = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
    # platforms = json.loads(response.content, object_hook=lambda p: SimpleNamespace(**p))
    # for yearly in years:
    #         if yearly.year is not None:
    #                 if yearly.year > 2013:
    #                         for platform_cons in platforms:
    #                                 print(str(yearly.year) + ' ' + platform_cons.platform)

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
    # else:
    #  print("No sales this year")
    # for sale_year in year:

    url = 'https://api.dccresource.com/api/games'
    data = urllib.request.urlopen(url).read().decode()
    obj = json.loads(data)

    lst2013 = []
    list_unknown_year = []
    for ob in obj:
        if ob['year'] is None:
            list_unknown_year.append(ob)
        elif ob['year'] >= 2013:
            lst2013.append(ob)

    return render_template('videogame/index.html', labels=labels, values=values)

# video_game.py
# register a blueprint
# create one endpoint
# visit it, go from there
