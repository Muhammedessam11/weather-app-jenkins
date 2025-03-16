import os
import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)
api_key = os.getenv("61989b9a02308991bb4b9050fb47231e")  # Load API key from environment

@app.route('/')
def home():
    return '''
        <form action="/weather" method="post">
            <label>Enter city name:</label>
            <input type="text" name="city">
            <input type="submit" value="Get Weather">
        </form>
    '''

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Weather in {city}: {weather}, Temperature: {temperature}°C"
    else:
        return "City not found."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

