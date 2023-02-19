from flask import Flask


app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    with open('requirements.txt') as reqs:
        return reqs.read()

