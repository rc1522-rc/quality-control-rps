
# Quality Control Exercise

This repository contains my Quality Control exercise for OPAN 3244.

The application is a simple Rock Paper Scissors game where the user plays against the computer. It also includes automated tests and continuous integration using GitHub Actions.

## Setup Instructions

First, clone this repository from GitHub or download it using GitHub Desktop.

Navigate to the repository folder using Terminal.

Create a virtual environment with Python 3.11:

```bash
conda create -n quality-control-env python=3.11
```

Activate the environment:

```bash
conda activate quality-control-env
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the example Python script:

```bash
python app/my_script.py
```

To play Rock Paper Scissors:

```bash
python -m app.rps
```

The game will ask the user to choose rock, paper, or scissors. The computer randomly chooses its option and the program determines the winner.

## Automated Testing

I used pytest to test the winner determination function.

To run the tests:

```bash
python -m pytest
```

The tests check all nine possible combinations of the game, including ties, user wins, and computer wins.

## Continuous Integration

This project uses GitHub Actions to run automated tests.

The workflow installs the packages from requirements.txt and runs pytest when a Pull Request is opened against the main branch or changes are pushed to main.

## Project Files

- app/my_script.py: Basic Python example
- app/rps.py: Rock Paper Scissors game
- test/rps_test.py: Automated tests for the game
- requirements.txt: Required Python packages
- .gitignore: Files excluded from GitHub
- .github/workflows/python-app.yml: GitHub Actions workflow





## Stocks Dashboard - Extra Credit

I also implemented a stocks dashboard using the Alpha Vantage API.

The application retrieves historical daily stock prices using pandas and displays a line chart using Plotly.

### API Key Setup

Get an API key from:

https://www.alphavantage.co/support/#api-key

Create a `.env` file in the main project directory.

Add:

```text
ALPHAVANTAGE_API_KEY="YOUR_API_KEY"
```

Replace YOUR_API_KEY with your actual API key.

The `.env` file is excluded from version control using `.gitignore`.

GitHub Actions uses a repository secret named `ALPHAVANTAGE_API_KEY` to run the automated stocks test.

### Running the Dashboard

Activate the environment:

```bash
conda activate quality-control-env
```

Install the packages:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
python -m app.stocks
```

Enter a stock ticker such as IBM when prompted.

### Testing

Run all tests using:

```bash
python -m pytest
```

The stocks test checks that the data-fetching function returns a pandas DataFrame containing timestamp and closing-price columns.

This test requires a valid API key and available access to the Alpha Vantage API.
