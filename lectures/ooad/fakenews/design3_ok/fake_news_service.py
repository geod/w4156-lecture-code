import logging
from flask import Flask
from flask import jsonify
from flask import request
from lectures.ooad.fakenews.design3_ok.scorer import ScorerFactory

app = Flask(__name__)

scorer = None


def init():
    global scorer
    scorer_factory = ScorerFactory()
    scorer = scorer_factory.create(app.config['DATA_DIR'])


@app.route('/fakenews')
def score_url():
    newsurl = request.args.get('newsurl')
    result = scorer.score_domain(newsurl)
    return jsonify({'score': result, 'code': "SUCCESS"})


if __name__ == '__main__':
    logging.info("Starting Suggestion Service")
    app.run(port=5000, debug=True)
