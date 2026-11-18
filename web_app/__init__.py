
import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.rps_routes import rps_routes
from web_app.routes.stocks_routes import stocks_routes

load_dotenv()


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY", "development-secret"
    )

    app.register_blueprint(home_routes)
    app.register_blueprint(rps_routes)
    app.register_blueprint(stocks_routes)

    return app
