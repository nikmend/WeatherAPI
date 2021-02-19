from flask import (
    Flask, request
)
import json
from weather.openweathermap import get_weather

app = Flask(__name__)


@app.route('/')
def index():
    return 'this is my weather API!'


@app.route('/weather', methods=['GET'])
def weather():
    try:
        if request.method == 'GET':
            """
            city=$City&country=$Country
            """
            city = request.args.get('city')
            country = request.args.get('country')
            print(city, country)
            data = get_weather(cityName=city, isoCountry=country)
            response = app.response_class(
                response=json.dumps(data.__dict__),
                status=200,
                mimetype='application/json'
            )
            return response

    except Exception as e:
        return json.dumps({'error': str(e)})


app.run()
