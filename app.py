from flask import Flask, jsonify, request, session
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)


@app.route('/survey/budget/', methods=['POST'])
def budget():
    try:
        budget_value = request.get_json().get('budget', None)
        session['budget_value'] = budget_value
        return jsonify({'success': True, 'received': budget_value})
    except:
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
