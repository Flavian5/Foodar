from flask import Flask, jsonify, request, session
from flask_cors import CORS
import traceback
from menu_constants import menu, structured_menu

app = Flask(__name__)
CORS(app)


@app.route('/menu/', methods=['POST'])
def menu_page():
    try:
        top_choices = request.get_json().get('top_food_choices', None)
        recommended = request.get_json().get('food_recommend_by_your_friends', None)
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


@app.route('/survey/budget/', methods=['POST'])
def budget():
    try:
        budget_value = request.get_json().get('budget', None)
        session['budget_value'] = budget_value
        return jsonify({'success': True, 'received': budget_value})
    except:
        traceback.print_exc()
        return jsonify({'success': False})


@app.route('/survey/<food_region>_food/', methods=['POST'])
def types_of_food():
    try:
        food_types = request.get_json().get('food_type', None)
        session['food_type'] = food_types
        return jsonify({'success': True, 'received': food_types})
    except:
        traceback.print_exc()
        return jsonify({'success': False})


@app.route('/survey/food_region/', methods=['POST'])
def food_region():
    try:
        food = request.get_json().get('food_region', None)
        session['food_region'] = food
        return jsonify({'success': True, 'received': food})
    except:
        traceback.print_exc()
        return jsonify({'success': False})


@app.route('/survey/meal_type/', methods=['POST'])
def meal_type():
    try:
        received = request.get_json().get('meal_type', None)
        session['meal_type'] = received
        return jsonify({'success': True, 'received': received})
    except:
        traceback.print_exc()
        return jsonify({'success': False})


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'success': True})


if __name__ == "__main__":
    app.secret_key = 'the music app sucks'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host="localhost", port=5000, debug=True)
