import json, requests
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from types import SimpleNamespace
import urllib.request

bp = Blueprint('videogame', __name__)


@bp.route('/', methods=['GET'])
def index():
    response = requests.get('https://api.dccresource.com/api/games')
    data = json.loads(response.content)
    # goal : Get all unique platforms
    unique_platofrms = {}
    game_data = json.loads(response.content, object_hook=lambda g: SimpleNamespace(**g))

    for game in game_data:
        game_platform = game.platform
        if game.year is not None and game.year > 2012:
            if game_platform not in unique_platofrms:
                unique_platofrms[game_platform] = game.globalSales
            else:
                unique_platofrms[game_platform] += game.globalSales

    global_sales_list = []
    for key in unique_platofrms:
        global_sales_list.append((unique_platofrms[key], key))
    global_sales_list = sorted(global_sales_list, key=lambda x: -x[0])
    labels = []
    values = []
    for game_platform in global_sales_list:
        values.append(game_platform[0])
        labels.append(game_platform[1])
    return render_template("videogame/index.html", labels=labels, values=values)


@bp.route('/', methods=['POST'])
def game_details():
    if request.method == 'POST':
        page_title = request.form['title']
        error = None

        if not page_title:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        else:
            response = requests.get('https://api.dccresource.com/api/games')
            data = json.loads(response.content)
            # goal : Get all unique platforms
            unique_platofrms = {}
            game_data = json.loads(response.content, object_hook=lambda g: SimpleNamespace(**g))

            searched_game = None
            for game in game_data:

                if game.name is not None and game.name == page_title:
                    searched_game = game

            return render_template('videogame/videoGameDetails.html', page_title=page_title, searched_game=searched_game)

    else:
        return render_template('videogame/videoGameDetails.html', page_title="PostForm from Module Function")
