from flask import Flask, request

from weather_app.greeting import greet

app = Flask(__name__)


@app.route('/')
def main():
    ip_address = request.headers['X-Forwarded-For']

    return greet(ip_address)


if __name__ == '__main__':
    app.run()
