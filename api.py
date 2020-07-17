# Class contains API functionalities

from flask import Flask, redirect, url_for, render_template
from pipelines import CovidapiPipeline

from flask import Flask, request, url_for, jsonify

app = Flask(__name__)

database = CovidapiPipeline()


@app.route('/query')
def get_country_data():
    country = request.args.get('country')
    return '<h1>Data: {}</h1'.format(database.get_data(country))


if __name__ == '__main__':
    app.run(debug=True)
