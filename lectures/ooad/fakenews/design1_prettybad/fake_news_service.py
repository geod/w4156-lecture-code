from .indicators import *
import logging

from flask import Flask
from flask import request, json
from flask import render_template, send_from_directory
app = Flask(__name__)


@app.route('/fakenews')
def score_url(newsurl):
    content_scorer = ContentScorer()
    whitelist_scorer = WhitelistScorer()
    whois_scorer = WhoisScorer()

    content_score = content_scorer.score_domain(newsurl)
    whitelist_score = whitelist_scorer.score_domain(newsurl)
    whois_score = whois_scorer.score_domain(newsurl)

    score = content_score + whitelist_score + whois_score / 3

    return json({'score': score})


if __name__ == '__main__':
    logging.info("Starting Suggestion Service")
    app.run(port=5000, debug=True)
