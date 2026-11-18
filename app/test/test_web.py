
from web_app import create_app


app = create_app()


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_about():
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200


def test_hello():
    client = app.test_client()
    response = client.get("/hello?name=Alex")
    assert response.status_code == 200
    assert b"Hello, Alex!" in response.data


def test_rps_form():
    client = app.test_client()
    response = client.get("/rps/form")
    assert response.status_code == 200


def test_rps_results():
    client = app.test_client()
    response = client.post(
        "/rps/results",
        data={"choice": "rock"}
    )
    assert response.status_code == 200
    assert b"You chose:" in response.data


def test_stocks_form():
    client = app.test_client()
    response = client.get("/stocks/form")
    assert response.status_code == 200


def test_invalid_stock():
    client = app.test_client()
    response = client.post(
        "/stocks/dashboard",
        data={"symbol": ""},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Please enter a stock symbol." in response.data
