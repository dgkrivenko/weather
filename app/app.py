from flask import Flask
from cache import cache


app = Flask(__name__)


@app.route('/')
def get_humidity():
    return cache.get_humidity()


if __name__ == '__main__':
    app.run()
