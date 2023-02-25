from flask import request, render_template, Blueprint
from faker import Faker
import pandas as pd
import requests


bp = Blueprint('main', __name__)


@bp.route("/")
def learning_flask():
    return render_template("main_html/root_page.html")


@bp.route("/requirements/")
def requirements():
    with open("../requirements.txt") as reqs:
        req_s = reqs.read()
        return render_template("main_html/requirements.html", text=req_s.split('\n')[:-1])


@bp.route("/generate-users/")
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
    return render_template("main_html/generate_users.html", list_users=users)


@bp.route("/mean/")
def average():
    data = pd.read_csv("../hw.csv")
    data.columns = ["Index", "Height(Inches)", "Weight(Pounds)"]
    avr_height_cm = data.mean()[1] * 2.54
    avr_weight_kg = data.mean()[2] * 0.4536
    return render_template("main_html/mean.html", mhc=avr_height_cm, mwk=avr_weight_kg)


@bp.route("/space/")
def cosmonauts():
    r = requests.get("http://api.open-notify.org/astros.json")
    result = r.json()["number"]
    return render_template("my_app_html/space.html", number=result)
