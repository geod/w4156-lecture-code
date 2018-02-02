import logging

from flask import Flask, json
import requests
import whois
import datetime

app = Flask(__name__)

whitelist = {}
with open('whitelist.txt') as f:
    entry = f.readline()
    domain, score = entry.split(",")[0], [1]
    whitelist[domain] = score

keywords = []
with open('keywords.txt') as f:
    kw = f.readline()
    keywords.append(kw)


@app.route('/fakenews')
def score_url(newsurl):
    # whitelisting of the domain
    whitelist_score = 0.5
    whitelist_score = whitelist.get(newsurl, whitelist_score)

    # what is the content of the page
    content_score = 0.5
    r = requests.get(newsurl)
    if r.status_code == 200:
        for keyword in keywords:
            if keyword in r.text:
                content_score = max(content_score - 0.1, 0)

    # whois the domain (age)
    domain_score = 0.5
    domain = whois.query(newsurl)
    if domain is not None:
        daysalive = (datetime.datetime.now() - domain.creation_date).days
        # 0 days is 0, 365 is 0.5, 730 is 1
        domain_score = min(daysalive, 730) / 730

    score = (whitelist_score + content_score + domain_score) / 3

    return json({'score': score})


if __name__ == '__main__':
    logging.info("Starting Suggestion Service")
    app.run(port=5000, debug=True)
