from .indicators import *
import logging

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

scorer = None


def init():
    print("INIT")
    data_dir = app.config['DATA_DIR']
    global scorer
    scorer = ScorerFactory().create(baseconfigdir=data_dir)


@app.route('/fakenews')
def score_url():
    newsurl = request.args.get('newsurl')
    result = scorer.score_domain(newsurl)
    return jsonify({'score': result, 'code': "SUCCESS"})

if __name__ == '__main__':
    logging.info("Starting Suggestion Service")
    app.run(port=5000, debug=True)
