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

## Loading Data Into SQLite

### Using sqlite-utils
You can load the JSON data into whatever backend you want. One easy way to load it
into SQLite is using [sql-utils](https://sqlite-utils.datasette.io/en/stable/index.html):
1. `pip install sqlite-utils`
2. `sqlite-utils insert oreilly.db books oreilly.json`

### Using the json-to-sqlite Scripts
In the `json-to-sqlite` subfolder you'll find three scripts which can be used to:
1. Add a unique integer to each book record in `oreilly.json`: `add_pid_to_json.py`
2. Create a SQLite DB to contain the data from `oreilly.json`: `create_db.py`
3. Transform the JSON data from `oreilly.json` into rows of data in the new SQLite DB: `convert_json_to_tables.py`

## Quirks

### Excluding Fields
You can exclude fields from the results returned by the API but only some fields. For example, 'archive_id' can be excluded but 'num_of_followers' cannot.

You can find a complete list of the excludable fields here: https://www.oreilly.com/online-learning/integration-docs/search.html#/get~api~v2~search~5