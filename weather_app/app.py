import os

from flask import Flask, request

from weather_app.greeting import greet, get_local_IP_address

app = Flask(__name__)

DEPLOY = os.environ.get('DEPLOY')


@app.route('/')
def main():
    if DEPLOY == 'heroku':
        ip_address = request.headers['X-Forwarded-For']
    else:
        ip_address = get_local_IP_address()

    return greet(ip_address)


if __name__ == '__main__':
    app.run()
