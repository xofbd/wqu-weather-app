import os
from flask import Flask, request, render_template
from weather_app.utils import greet, get_external_IP_address

app = Flask(__name__)
DEPLOY = os.environ.get('DEPLOY')


@app.route('/')
def main():
    if DEPLOY == 'heroku':  # env variable set when deploying to heroku
        ip_address = request.headers['X-Forwarded-For']
    else:  # `DEPLOY == local` when running locally
        # Get an IP other than 'localhost' or '127.0.0.1'
        ip_address = get_external_IP_address()

    return render_template('index.html', weather_info=greet(ip_address))


if __name__ == '__main__':
    app.run()
