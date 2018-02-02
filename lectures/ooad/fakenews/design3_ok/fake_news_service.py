from .indicators import *
import logging

from flask import Flask
from flask import json
app = Flask(__name__)

scorer = ScorerFactory().create()


@app.route('/fakenews')
def score_url(newsurl):
    score = scorer.score_domain(newsurl)
    return json({'score': score})


if __name__ == '__main__':
    logging.info("Starting Suggestion Service")
    app.run(port=5000, debug=True)
