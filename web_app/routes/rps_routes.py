
import random

from flask import Blueprint, render_template, request, redirect, url_for

from app.rps import determine_winner, VALID_OPTIONS


rps_routes = Blueprint("rps_routes", __name__)


@rps_routes.route("/rps/form")
def rps_form():
    return render_template("rps_form.html")


@rps_routes.route("/rps/results", methods=["POST"])
def rps_results():

    user_choice = request.form.get("choice")

    if user_choice not in VALID_OPTIONS:
        return redirect(url_for("rps_routes.rps_form"))

    computer_choice = random.choice(VALID_OPTIONS)

    result = determine_winner(user_choice, computer_choice)

    return render_template(
        "rps_results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result
    )
