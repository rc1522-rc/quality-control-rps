import os

from pandas import read_csv
from dotenv import load_dotenv
import plotly.express as px


load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


def fetch_stocks_csv(symbol="IBM"):

    request_url = (
        "https://www.alphavantage.co/query?"
        f"function=TIME_SERIES_DAILY&symbol={symbol}"
        f"&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    )

    stocks_df = read_csv(request_url)

    return stocks_df


if __name__ == "__main__":

    symbol = input("Please choose a stock symbol: ") or "IBM"

    stocks_df = fetch_stocks_csv(symbol)

    print(stocks_df.head())

    fig = px.line(
        stocks_df,
        x="timestamp",
        y="close",
        title=f"Stock Prices ({symbol})",
        height=450
    )

    fig.show()