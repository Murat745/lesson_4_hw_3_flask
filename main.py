from flask import Flask, request
from faker import Faker

app = Flask(__name__)


@app.route("/")
def learning_flask():
    return "<p> <h1>Here I'm going to learn Flask</h1> </p>"


@app.route('/requirements/')
def requirements():
    with open('requirements.txt') as reqs:
        return reqs.read()


@app.route("/generate-users/")
def user_dict():
    fake = Faker()
    users = {}
    quantity = 100
    args = request.args
    if args.get('quantity'):
        quantity = int(args.get('quantity'))
    for i in range(quantity):
        full_name = fake.name()
        first_name = full_name.split()[0]
        last_name = full_name.lower().split()[1]
        users[first_name] = f'{last_name}@mail.com'
    return users
