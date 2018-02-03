import logging

from flask import Flask, json
import requests
import whois
from datetime import date
import csv
from bs4 import BeautifulSoup

app = Flask(__name__)

whitelist = {}
with open('whitelist.txt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csvreader:
        whitelist[row[0].lower()] = float(row[1])

keywords = []
with open('keywords.txt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csvreader:
        keywords.append(row[0])


@app.route('/fakenews')
def score_url(newsurl):
    # whitelisting of the domain
    if newsurl is None:
        raise ValueError('Requires valid URL')
    whitelist_score = 0.5
    whitelist_score = whitelist.get(newsurl.lower(), whitelist_score)

    # what is the content of the page
    content_score = 0.5
    r = requests.get(newsurl)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text)
        text = soup.get_text().lower()
        for keyword in keywords:
            if keyword in text:
                content_score = max(content_score - 0.1, 0)

    # whois the domain (age)
    domain_score = 0.5
    domain = whois.query(newsurl)
    if domain is not None:
        today = date.today()
        daysalive = (today - domain.creation_date)
        # 0 days is 0, 365 is 0.5, 730 is 1
        domain_score = min(max(0, daysalive.days), 730) / 730

    score = (whitelist_score + content_score + domain_score) / 3

    return json({'score': score})


if __name__ == '__main__':
    logging.info("Starting Suggestion Service")
    app.run(port=5000, debug=True)
