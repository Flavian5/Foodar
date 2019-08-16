from flask import Flask, jsonify, request, session
from flask_cors import CORS
# from services.PlaidService import PlaidService
from services.GooglePlaceService import GooglePlaceService
import traceback
from menu_constants import menu, structured_menu

app = Flask(__name__)
CORS(app)

SURVEY_DATA = dict()
SURVEY_DATA['American'] = ['burger', 'pub', 'wings', 'tacos', 'burrito']
SURVEY_DATA['European'] = ['Italian', 'French', 'German/Austrian', 'Spanish']
SURVEY_DATA['Middle Eastern'] = ['Hummus', 'Falafel', 'Tabouleh', 'Fattoush', 'Shawarma', 'Kebab']
SURVEY_DATA['Asian'] = ['Japanese', 'Korean', 'Thai', 'Indian', 'Korean']


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
        if "meal_type" in request.get_json():
            session['meal_type'] = list(request.get_json().get('meal_type', None))
        if "food_region" in request.get_json():
            session['food_region'] = list(request.get_json().get('food_region', None))
        if "food_type" in request.get_json():
            session['food_type'] = list(request.get_json().get('food_type', None))
        if "budget_value" in request.get_json():
            session['budget_value'] = list(request.get_json().get('budget_value', None))

        if (session.get('meal_type') is None) and (session.get('food_region') is None) and (session.get('food_type') is None) \
                and (session.get('budget_value') is None):
            # In case there's nothing set for session
            session['meal_type'] = ['Vegetarian']
            session['food_region'] = ['European']
            session['food_type'] = ['Italian']
            session['budget_value'] = ['$$$']

        return jsonify({"success": True})
    except:
        traceback.print_exc()
        return jsonify({'success': False})


@app.route('/recommend', methods=['GET'])
def list_recommendations():
    """Based on the session variable values, including survey results, bank balances, get lists
    of restaurants from Google Places API, and combine & return the results"""
    gps = GooglePlaceService()
    # Step 1
    # Pulling in the survey results, and turn them into search queries
    base_restaurant_type = session['food_region'][0] + " restaurant"
    query_strings = [meal_type + " " + base_restaurant_type for meal_type in session['meal_type']]
    extended_query_strings = []
    for food_type in session['food_type']:
        extended_query_strings = extended_query_strings + [query + " " + food_type for query in query_strings]

    final_query_strings = []
    for budget_value in session['budget_value']:
        if budget_value in ["$", "$$"]:
            final_query_strings = final_query_strings + [query + " " + "cheap" for query in extended_query_strings]
        elif budget_value in ['$$$']:
            final_query_strings = final_query_strings + [query + " " + "expensive" for query in extended_query_strings]

    print(final_query_strings)
    total_results = []
    for query in final_query_strings:
        total_results = total_results + gps.search(query)
        break  # Just to check and make sure we have the data format correctly

    print(len(total_results))
    print(total_results[0])
    # Step 2
    # Parse the results and get an idea

    # Step 3
    # Combine the list of restaurant results

    # Step 4
    # Regeneration
    return jsonify({"success": True})


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'success': True})


if __name__ == "__main__":
    app.secret_key = 'the music app sucks'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host="localhost", port=5000, debug=True)
