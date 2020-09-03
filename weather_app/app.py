import os
from flask import Flask, request, render_template
from weather_app.greeting import greet, get_local_IP_address

app = Flask(__name__)
DEPLOY = os.environ.get('DEPLOY')


@app.route('/')
def main():
    if DEPLOY == 'heroku':
        ip_address = request.headers['X-Forwarded-For']
    else:
        ip_address = get_local_IP_address()

    return render_template('index.html', weather_info=greet(ip_address))


if __name__ == '__main__':
    app.run()
