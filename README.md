# O'Reilly Learning API Scraper

## Description
A primitive Python script that pulls down all the available books from the
O'Reilly Learning API and saves them to a local directory.

## Usage
1. Clone the repository
2. Install pipenv: `pip install pipenv`
3. Install dependencies and create virtual environment: `pipenv install`
4. Tweak any settings you want in `main.py`
5. Run the script: `python main.py`

## How It Works
It adds each page of results from the O'Reilly API to a Python dictionary
then writes that dictionary out to a JSON file.

## Why It Works This Way
Each page of results is its own contained JSON, we could concatenate
the JSON manually, but adding it to the dictionary is easier.