
from flask import Blueprint, render_template, request, redirect, url_for, flash
import plotly.express as px

from app.stocks import fetch_stocks_csv


stocks_routes = Blueprint("stocks_routes", __name__)


@stocks_routes.route("/stocks/form")
def stocks_form():
    return render_template("stocks_form.html")


@stocks_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def stocks_dashboard():

    symbol = (
        request.form.get("symbol")
        or request.args.get("symbol")
        or ""
    ).strip().upper()

    if not symbol or not symbol.replace(".", "").replace("-", "").isalnum():
        flash("Please enter a stock symbol.", "warning")
        return redirect(url_for("stocks_routes.stocks_form"))


    try:
        stocks_df = fetch_stocks_csv(symbol)

        if stocks_df.empty:
            raise ValueError("No stock data found")

        if "timestamp" not in stocks_df.columns or "close" not in stocks_df.columns:
            raise ValueError("Invalid stock data")

        stocks_df = stocks_df.sort_values(
            "timestamp", ascending=False
        )

        recent_data = stocks_df.head(10).to_dict("records")

        chart_df = stocks_df.sort_values("timestamp")

        fig = px.line(
            chart_df,
            x="timestamp",
            y="close",
            title=f"Stock Prices ({symbol})",
            height=450
        )

        chart = fig.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        )

        return render_template(
            "stocks_dashboard.html",
            symbol=symbol,
            data=recent_data,
            chart=chart
        )

    except Exception as err:
        print("STOCKS ERROR:", err)

        flash(
            "Could not find stock data. Check the symbol or try again later.",
            "warning"
        )

        return redirect(url_for("stocks_routes.stocks_form"))
