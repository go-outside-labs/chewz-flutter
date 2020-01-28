# Doordash API Scrapper

Quick script to pull basic business info out of yelp api and doordash endpoints.


## Install

This code requires Python 3.4 or higher and [requests](https://github.com/requests/requests).

Install from source:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python setup.py install
```

## Generating a report from CLI

Fill in global variables on top of `fud_report/fud_report.py` and run:

```python
fud_report
```

## TODO

* add examples for reponses & requests

## Enpoints

* [Business API](https://www.yelp.com/developers/documentation/v3/business) - `business_query(...)`
* [Search API](https://www.yelp.com/developers/documentation/v3/business_search) - `search_query(...)`
