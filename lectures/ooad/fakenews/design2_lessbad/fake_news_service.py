from .indicators import *
import logging

from flask import Flask
from flask import request, json
from flask import render_template, send_from_directory
app = Flask(__name__)


aggregator = AggregateScorer()
aggregator.add_scorer(ContentScorer())
aggregator.add_scorer(WhitelistScorer())
aggregator.add_scorer(WhoisScorer())


@app.route('/fakenews')
def score_url(newsurl):
    score = aggregator.score_domain(newsurl)
    return json({'score': score})

if __name__ == '__main__':
    logging.info("Starting Suggestion Service")
    app.run(port=5000, debug=True)
