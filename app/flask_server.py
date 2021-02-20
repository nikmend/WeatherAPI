from flask import (
    Flask, request, jsonify
)
from flask_caching import Cache
import json
from app.openweathermap import get_weather



app = Flask(__name__)
config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 120
}
app.config.from_mapping(config)
cache = Cache(app)


@app.route('/')
def index():
    return jsonify('this is my app API!')

@app.route('/weather', methods=['GET'])
@cache.cached(timeout=120)
def weather():
    try:
        if request.method == 'GET':
            """
            city=$City&country=$Country
            """
            city = request.args.get('city')
            country = request.args.get('country')

            data = get_weather(city_name=city, isoCountry=country)
            response = app.response_class(
                response=json.dumps(data.__dict__),
                status=200,
                mimetype='application/json'
            )
            return response

    except Exception as e:
        return json.dumps({'error': str(e)})

