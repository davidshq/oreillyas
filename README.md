# O'Reilly Learning API Scraper

## Description
A primitive Python script that pulls down all the available books from the
O'Reilly Learning API and saves them to a local directory.

> NOTE: You have to have an authentication token from O'Reilly in order to pull down more
> than the first five pages.

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

> NOTE: This works for a limited number of items, at some point `sql-utils` errors out, for importing larger numbers of records to SQLite see the section below.

### Using the json-to-sqlite Scripts
In the `json-to-sqlite` subfolder you'll find three scripts which can be used to:
1. Add a unique integer (pid) to each book record in `oreilly.json`: `add_pid_to_json.py`
2. Create a SQLite DB and appropriate tables to contain the data from `oreilly.json`: `create_db.py`
3. Transform the JSON data from `oreilly.json` into rows of data in the new SQLite DB: `convert_json_to_tables.py`

## How To: Generate a Sample from JSON results
The O'Reilly API results can get quite large (well over 100 MB) and can be a bit hard to manipulate in a GUI editor. You may want to run `generate_sample_from_json.py` after running `main.py`. This will take the first 400 records (you can customize the number) and place them in a separate json file that still gives a good idea of what the results are but in a more manageable size.

## Quirks

### Excluding Fields
You can exclude fields from the results returned by the API but only some fields. For example, 'archive_id' can be excluded but 'num_of_followers' cannot.

You can find a complete list of the excludable fields here: https://www.oreilly.com/online-learning/integration-docs/search.html#/get~api~v2~search~5

## Secondary Documentation / Scripts

The folder `for-learning` contains some additional scripts that show me exploring the O'Reilly API.

The folder `generic-json-mapping` is essentially nothing yet. I was surprised by the lack of a generic, essentially code free tool to convert JSON to a relational SQL DB. This is where I may eventually build something to handle that generic scenario (if it really starts to happen it'll probably be broken out into it's own repo).

## Credits
In some files I have explicitly noted this and while not required I'll do so anyways. I've used GitHub Copilot quite a bit in creating this project. I haven't messed around with it much before and this seemed like a good opportunity to see what I could get it to do. It can be quite frustrating at times, but I see potential.