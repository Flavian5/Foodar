from flask import Flask, jsonify, request, session
from flask_cors import CORS
from services.PlaidService import PlaidService
from services.GooglePlaceService import GooglePlaceService
import traceback
from menu_constants import menu, structured_menu

app = Flask(__name__)
CORS(app)


@app.route('/menu/', methods=['POST'])
def menu_page():
    try:
        top_choices = request.get_json().get('top_food_choices', None)
        recommended = request.get_json().get('food_recommended_by_your_friends', None)
        menu_items = request.get_json().get('menu_items', None)
        top_choices_prices = []
        top_choices_total_price = 0
        for choice in top_choices:
            price = menu.get(choice, '-99999$')
            top_choices_prices.append(price)
            top_choices_total_price += float(price.rstrip('$'))
        recommended_prices = []
        recommended_total_price = 0
        for rec in recommended:
            price = menu.get(rec, '-99999$')
            recommended_prices.append(price)
            recommended_total_price += float(price.rstrip('$'))
        menu_items_prices =[]
        menu_items_total_price = 0
        for item in menu_items:
            price = menu.get(item, '-99999$')
            menu_items_prices.append(price)
            menu_items_total_price += float(price.rstrip('$'))
        session['top_choices_prices'] = top_choices_prices
        session['top_choices_total_price'] = top_choices_total_price
        session['recommended_prices'] = recommended_prices
        session['recommended_total_price'] = recommended_total_price
        session['menu_items_prices'] = menu_items_prices
        session['menu_items_total_price'] = menu_items_total_price
        return jsonify({'success': True, 'menu': structured_menu, 'top_choices_price': top_choices_prices,
                        'top_choices_total_price': top_choices_total_price, 'recommended_prices': recommended_prices,
                        'recommended_total_price': recommended_total_price, 'menu_items_prices': menu_items_prices,
                        'menu_items_total_price': menu_items_total_price})
    except:
        traceback.print_exc()
        return jsonify({'success': False})


@app.route('/survey', methods=['POST'])
def survey():
    try:
        meal_type = request.get_json().get('meal_type', None)
        session['meal_type'] = meal_type
        food = request.get_json().get('food_region', None)
        session['food_region'] = food
        food_type = request.get_json().get('food_type', None)
        session['food_type'] = food_type
        budget_value = request.get_json().get('budget', None)
        session['budget_value'] = budget_value
        return jsonify({'success': True, 'meal_type': meal_type, 'food_region': food, 'food_type': food_type,
                        'budget': budget_value})
    except:
        traceback.print_exc()
        return jsonify({'success': False})


@app.route('/recommend', methods=['GET'])
def list_recommendations():
    """Based on the session variable values, including survey results, bank balances, get lists
    of restaurants from Google Places API, and combine & return the results"""
    gps = GooglePlaceService()
    return gps.search("japanese restaurants") # Place holder


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'success': True})


if __name__ == "__main__":
    app.secret_key = 'the music app sucks'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host="localhost", port=5000, debug=True)
