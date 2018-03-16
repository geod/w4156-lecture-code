## Object Oriented Analysis

### Hmmmm

At this stage the code isn't bad. It reads pretty easily. I can add or remove new scorers.

But what I still dont like is that flask knows too much about the scorers.
 1. It knows about the aggregate and also each one in the list
 2. If I want to add or remove scorers then I do it in flask
 3. What if I wanted to run two versions of the service with different scorers running? I can't do that because it is hard coded and flask 'knows'

```python
aggregator = AggregateScorer()
aggregator.add_scorer(ContentScorer())
aggregator.add_scorer(WhitelistScorer())
aggregator.add_scorer(WhoisScorer())

@app.route('/fakenews')
def score_url(newsurl):
    score = aggregator.score_domain(newsurl)
    return json({'score': score})
```

### The missing concept?

```python
aggregator = AggregateScorer()
aggregator.add_scorer(ContentScorer())
aggregator.add_scorer(WhitelistScorer())
aggregator.add_scorer(WhoisScorer())
```
##### Why do I dislike this code?
I dislike this block of code because I am exposing too much to flask. I don't want flask to know that the scorer is really an aggregator that contains 3 scorers

##### What is it doing?
In the most basic description this block of code is 'making the aggregate scorer, all the individual scorers and plugging them together'

##### How do I fix it? 
Ok - so I want to *encapsulate* this 'making' code somehow ......

But how do I do this?

Ewan said something about OOAD. What was it?
- Was it everything was an Orangutan? No no. That wasn't it.
- Was it everything was an Orange. No. That wasn't it either.
- **I remember! everything is an object**!
 
##### Factories make things?

Our thought progression is
1. We want to encapsulate the logic which makes/creates the scorer
2. Everything is an object
3. Factories make things

So lets create a class called *ScorerFactory* which makes scorers!

```python
class ScorerFactory:
    """
    This is not a scorer (see the class signature)
    """

    def create(self, baseconfigdir="."):
        """
        Create a scorer
        :param baseconfigdir: configuration directory
        :return: a configured scorer
        """
        aggregator = AggregateScorer()
        aggregator.add_scorer(ContentScorer(baseconfigdir))
        aggregator.add_scorer(WhitelistScorer(baseconfigdir))
        aggregator.add_scorer(WhoisScorer())
        return aggregator
```

The way I would then use the ScorerFactory

```python
    scorer_factory = ScorerFactory()    
    scorer = scorer_factory.create(data_dir)
```

(Remember - it is an object that 'makes' other objects)

Let's now return to look at flask

```python
def init():
    global scorer
    scorer_factory = ScorerFactory()
    scorer = scorer_factory.create(app.config['DATA_DIR'])


@app.route('/fakenews')
def score_url():
    newsurl = request.args.get('newsurl')
    result = scorer.score_domain(newsurl)
    return jsonify({'score': result, 'code': "SUCCESS"})
```

- flask knows it has a factory which makes a scorer
- it uses a scorer to score a domain
- it marshalls the results back
- if we wanted to change how many scorers or weighting - we can change the factory
- if we want to add new scorers its easy
- we can test scorers independently

### Am I happy?
Yes

##### fixed issues

1. It is hard to test the scoring logic outside of flask
2. It is hard to test individual scoring logic (whitelist, content, domain) independent of each other
3. We do not associate data (whitelist and content keywords) with the function (the former is at the top, the latter is at the bottom)
4. There is a growing 'blob' of code within the handler. Right now it is almost readable but wont become readable if I add more scorers or make any one of them more complex
6. Not super easy to change the weighting of different scorers
5. Not super easy to add a new scorer
7. The webservice just knows too much. All it needs to know is there is something which scores a domain. We do not need to expose the messiness






