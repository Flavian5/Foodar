from flask import Flask, jsonify, request, session
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)
menu = {
    "Egg Mcmuffin Burger": "10.50$",
    "Beyond Meat Burger": "8.40$",
    "Tofu Burger": "8.00$",
    "Chickpea Burger": "11.00$",
    "Hashbrown": "5.00$",
    "French Fries": "6.00$",
    "Tofu Salad": "7.00$",
    "Vegan Pizza": "11.80$",
    "Vegan Mac and Cheese": "9.00$",
    "Spaghetti": "10.30$",
    "Lentil Soup": "7.50$",
    "Hummus Quesadillas": "9.30$"
}


@app.route('/menu/', methods=['POST'])
def menu_page():
    try:
        top_choices = request.get_json().get('top_food_choices', None)
        recommended = request.get_json().get('food_recommend_by_your_friends', None)
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
        return jsonify({'success': True, 'top_choices_price': top_choices_prices,
                        'top_choices_total_price': top_choices_total_price, 'recommended_prices': recommended_prices,
                        'recommended_total_price': recommended_total_price})
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
