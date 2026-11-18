
from flask import Blueprint, render_template, request

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template("home.html")


@home_routes.route("/about")
def about():
    return render_template("about.html")


@home_routes.route("/hello")
def hello():
    name = request.args.get("name") or "World"
    return render_template("hello.html", name=name)
