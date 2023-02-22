from flask import Flask, request
from faker import Faker
import pandas as pd
import requests


app = Flask(__name__)


@app.route("/")
def learning_flask():
    return "<p> <h1>Here I'm going to learn Flask</h1> </p>"


@app.route("/requirements/")
def requirements():
    with open("requirements.txt") as reqs:
        return reqs.read()


@app.route("/generate-users/")
def user_dict():
    fake = Faker()
    users = {}
    quantity = 100
    args = request.args
    if args.get("quantity"):
        quantity = int(args.get("quantity"))
    for i in range(quantity):
        full_name = fake.name()
        first_name = full_name.split()[0]
        last_name = full_name.lower().split()[1]
        users[first_name] = f"{last_name}@mail.com"
    return users


@app.route("/mean/")
def average():
    data = pd.read_csv("hw.csv")
    data.columns = ["Index", "Height(Inches)", "Weight(Pounds)"]
    avr_height_cm = data.mean()[1]
    avr_weight_kg = data.mean()[2]
    return f"Average height: {avr_height_cm}\nAverage weight: {avr_weight_kg}"


@app.route("/space/")
def cosmonauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    result = r.json()['number']
    return f'Number of cosmonauts - {result}'
