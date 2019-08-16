from flask import Flask, jsonify, url_for, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('survey/budget')
def budget(how_much):


@app.route('survey/asian_food')
def asian_food(selection):
    selected = {selection: selection}
    return redirect(url_for('budget'))


@app.route('survey/middle_eastern_food')
def middle_eastern_food(selection):
    return redirect(url_for('budget'))


@app.route('survey/european_food')
def european_food(selection):
    return redirect(url_for('budget'))


@app.route('survey/american_food')
def american_food(selection):
    return redirect(url_for('budget'))


@app.route('/survey/food_type')
def food_type(food):
    if food == 'American':
        return redirect(url_for('american_food'))
    elif food == 'European':
        return redirect(url_for('european_food'))
    elif food == 'Middle Eastern':
        return redirect(url_for('middle_eastern_food'))
    else:
        return redirect(url_for('asian_food'))


@app.route('/survey/meal_type')
def meal_type(selected):
    return redirect(url_for())


@app.route('/survey')
def survey():
    return redirect(url_for('meal_type'))


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'success': True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)