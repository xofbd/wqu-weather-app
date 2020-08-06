from flask import Flask, request

from greeting import greet

app = Flask(__name__)


@app.route('/')
def main():
    ip_address = request.environ['REMOTE_ADDR']
    print(ip_address)
    return greet(ip_address)


if __name__ == '__main__':
    app.run()
