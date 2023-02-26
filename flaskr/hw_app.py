from flask import request, render_template, Blueprint
from faker import Faker
import pandas as pd
import requests


bp = Blueprint('hw_app', __name__)
fake = Faker()


@bp.route("/")
def learning_flask():
    return render_template("root_page.html")


@bp.route("/requirements/")
def requirements():
    with open("flaskr/requirements.txt") as reqs:
        req_s = reqs.read()
        return render_template("requirements.html", text=req_s.split('\n')[:-1])


@bp.route("/generate-users/")
def user_dict():
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
        emails = f"{last_name}@mail.com"
    return render_template("generate_users.html", list_users=users, name=f"{fake.name().split()[0]}",
                           email=emails
                           )


@bp.route("/mean/")
def average():
    data = pd.read_csv("flaskr/hw.csv")
    data.columns = ["Index", "Height(Inches)", "Weight(Pounds)"]
    avr_height_cm = data.mean()[1] * 2.54
    avr_weight_kg = data.mean()[2] * 0.4536
    return render_template("mean.html", mhc=avr_height_cm, mwk=avr_weight_kg)


@bp.route("/space/")
def cosmonauts():
    r = requests.get("http://api.open-notify.org/astros.json")
    result = r.json()["number"]
    return render_template("space.html", number=result)
