from flask import Flask, jsonify, url_for, redirect, request, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('survey/budget/', method=['POST'])
def budget():
    session['budget'] = request.get_json().get('budget', None)
    return redirect(url_for('test'))  # TODO: change to whatever the next page will be


@app.route('survey/asian_food/', method=['POST'])
def asian_food():
    food_types = request.get_json().get('food_type', None)
    session['food_type'] = food_types
    return redirect(url_for('budget'))


@app.route('survey/middle_eastern_food/', method=['POST'])
def middle_eastern_food():
    food_types = request.get_json().get('food_type', None)
    session['food_type'] = food_types
    return redirect(url_for('budget'))


@app.route('survey/european_food/', method=['POST'])
def european_food():
    food_types = request.get_json().get('food_type', None)
    session['food_type'] = food_types
    return redirect(url_for('budget'))


@app.route('survey/american_food/', method=['POST'])
def american_food():
    food_types = request.get_json().get('food_type', None)
    session['food_type'] = food_types
    return redirect(url_for('budget'))


@app.route('/survey/food_region/', method=['POST'])
def food_type():
    food = request.get_json().get('food_region', None)
    session['food_region'] = food
    if food == 'American':
        return redirect(url_for('american_food'))
    elif food == 'European':
        return redirect(url_for('european_food'))
    elif food == 'Middle Eastern':
        return redirect(url_for('middle_eastern_food'))
    else:
        return redirect(url_for('asian_food'))


@app.route('/survey/meal_type/', method=['POST'])
def meal_type():
    session['meal_type'] = request.get_json().get('meal_type', None)
    return redirect(url_for('food_type'))


@app.route('/survey')
def survey():
    return redirect(url_for('meal_type'))


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'success': True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)