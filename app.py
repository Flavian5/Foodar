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
        top_choices = request.get_json().get('top_food_choices', [])
        recommended = request.get_json().get('food_recommended_by_your_friends', [])
        menu_items = request.get_json().get('menu_items', [])
        top_choices_prices = []
        top_choices_total_price = 0
        for choice in top_choices:
            price = menu.get(choice, '10$')
            top_choices_prices.append(price)
            top_choices_total_price += float(price.rstrip('$'))
        recommended_prices = []
        recommended_total_price = 0
        for rec in recommended:
            price = menu.get(rec, '10$')
            recommended_prices.append(price)
            recommended_total_price += float(price.rstrip('$'))
        menu_items_prices =[]
        menu_items_total_price = 0
        for item in menu_items:
            price = menu.get(item, '10$')
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
        # if "meal_type" in request.get_json():
        #     session['meal_type'] = list(request.get_json().get('meal_type', None))
        # if "food_region" in request.get_json():
        #     session['food_region'] = list(request.get_json().get('food_region', None))
        # if "food_type" in request.get_json():
        #     session['food_type'] = list(request.get_json().get('food_type', None))
        # if "budget_value" in request.get_json():
        #     session['budget_value'] = list(request.get_json().get('budget_value', None))
        #
        # if (session.get('meal_type') is None) and (session.get('food_region') is None) and (session.get('food_type') is None) \
        #         and (session.get('budget_value') is None):
        #     # In case there's nothing set for session
        #     session['meal_type'] = ['Vegetarian']
        #     session['food_region'] = ['European']
        #     session['food_type'] = ['Italian']
        #     session['budget_value'] = ['$$$']
        if not request.get_json():
            data = {
                'meal_type': ['Vegetarian'],
                'food_region': ["European"],
                'food_type': ["Italian"],
                'budget_value': ["$$$"]
            }
        else:
            data = {
                'meal_type': [request.get_json().get('meal_type', 'Vegetarian')],
                'food_region': [request.get_json().get('food_region', "European")],
                'food_type': [request.get_json().get('food_type', "Italian")],
                'budget_value': [request.get_json().get('budget_value', "$$$")]
            }
        list_recommendations(data)
        return jsonify({"success": True})
    except:
        traceback.print_exc()
        return jsonify({'success': False})


# @app.route('/recommend', methods=['GET'])
def list_recommendations(data):
    """Based on the session variable values, including survey results, bank balances, get lists
    of restaurants from Google Places API, and combine & return the results"""
    gps = GooglePlaceService()
    # Step 1
    # Pulling in the survey results, and turn them into search queries
    base_restaurant_type = data['food_region'][0] + " restaurant"
    query_strings = [meal_type + " " + base_restaurant_type for meal_type in data['meal_type']]
    extended_query_strings = []
    for food_type in data['food_type']:
        extended_query_strings = extended_query_strings + [query + " " + food_type for query in query_strings]

    final_query_strings = []
    for budget_value in data['budget_value']:
        if budget_value in ["$", "$$"]:
            final_query_strings = final_query_strings + [query + " " + "cheap" for query in extended_query_strings]
        elif budget_value in ['$$$']:
            final_query_strings = final_query_strings + [query + " " + "expensive" for query in extended_query_strings]

    print(final_query_strings)
    total_results = []
    for query in final_query_strings:
        total_results = total_results + [gps.search(query)]
        # break  # Just to check and make sure we have the data format correctly

    print(len(total_results))
    print(total_results[0])
    # Step 2
    # Parse the results and get an idea
    final_results = []
    for item in total_results:
        item_list = item['results']
        restaurant_details = dict()
        for restaurant in item_list:
            restaurant_details['name'] = restaurant['name']
            restaurant_details["formatted_address"] = restaurant["formatted_address"]
            restaurant_details['latitude'] = restaurant['geometry']['location']['lat']
            restaurant_details['longitude'] = restaurant['geometry']['location']['lng']
            photos = restaurant['photos']
            restaurant_details['photo_url'] = gps.get_photos(name=restaurant['name'],photo_reference=photos[0].get('photo_reference'))
            restaurant_details['price_level'] = restaurant.get('price_level', 2)
            restaurant_details['rating'] = restaurant['rating']
            restaurant_details['num_ratings'] = restaurant['user_ratings_total']
        final_results = final_results + [restaurant_details]

    return jsonify({"success": True, "results": final_results})


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'success': True})


if __name__ == "__main__":
    app.secret_key = 'the music app sucks'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host="0.0.0.0")
