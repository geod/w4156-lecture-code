## Object Oriented Analysis

### Another missing concept

If we look at the code from the previous design it is a bit ugly.
1. There is repetition (I have 3 lines all passing in the url). 
2. I could create a python list of scorers and iterate

```python
@app.route('/fakenews')
def score_url(newsurl):
    content_score = content_scorer.score_domain(newsurl)
    whitelist_score = whitelist_scorer.score_domain(newsurl)
    whois_score = whois_scorer.score_domain(newsurl)

    score = content_score + whitelist_score + whois_score / 3
    return json({'score': score})
```

3. However, the bottom line of code is interesting

```python
score = content_score + whitelist_score + whois_score / 3
```

What is going on here. Really this code says 'give each scorer the chance to score the URL then average the result'

I am missing a concept! Part of OO is looking at your code and seeing *missing* and *abstract* concepts.
 
 4. Therefore I decide to add an AggregatingScorer
 
 ```python
class AggregateScorer(AbstractDomainScorer):
    """
    A scorer which contains a list of scorers. When asked to score a URL it asks each scorer to provide a score then averages
    the result.

    Prepare for mind blown: AggregateScorer is also a scorer in that it implements the same contract of score_domain even though it
    behaves differently!!!!
    """

    def __init__(self):
        self.__scorers = []

    def add_scorer(self, scorer: AbstractDomainScorer):
        if scorer in self.__scorers:
            raise ValueError("Duplicate Scorer")
        self.__scorers.append(scorer)

    def score_domain(self, newsurl):
        scores = [None] * len(self.__scorers)
        for scorer in self.__scorers:
            scores.append(scorer.score_domain(newsurl))
        res = mean(scores)
        return res
```

5. Absorb this. The AggregateScorer is a scorer but with fundamentally different behavior.
6. It has a list of scorers
7. When asked to score the url it asks then averages the result
8. But come to think of it - it *is* still a Scorer because you can ask it to score a domain and it does!

```python
aggregator = AggregateScorer()
aggregator.add_scorer(ContentScorer())
aggregator.add_scorer(WhitelistScorer())
aggregator.add_scorer(WhoisScorer())


@app.route('/fakenews')
def score_url():
    newsurl = request.args.get('newsurl')
    score = aggregator.score_domain(newsurl)
    return json({'score': score})
```

### Am I happy?
Nope - still not happy:

##### fixed issues

1. It is hard to test the scoring logic outside of flask
2. It is hard to test individual scoring logic (whitelist, content, domain) independent of each other
3. We do not associate data (whitelist and content keywords) with the function (the former is at the top, the latter is at the bottom)
4. There is a growing 'blob' of code within the handler. Right now it is almost readable but wont become readable if I add more scorers or make any one of them more complex
6. Not super easy to change the weighting of different scorers

##### partially fixed
5. Not super easy to add a new scorer

(it is *much* easier in the sense I can add it to the aggregator but I still have to make changes in flask)

```python
aggregator.add_scorer(MyNewFancyScorer())
```

##### not fixed
7. The webservice just knows too much. All it needs to know is there is something which scores a domain. We do not need to expose the messiness

The web server/flask knows about the aggregator and configuration.

###### Disclaimer
This code isnt actually that bad and as a matter of taste some people may stop here. There is an argument for 'going nuts' over object orienting every problem. 
- If there was not a *requirement* to have flexibility in changing scorers then people may stop here.
- Personally, I may stop here until next time I touch the code and have to make the scorer flexible at which point I would do the next refactoring
- Again, this is the idea that code is not designed and written in 'one go'. Rather code is 'grown' through repeated accretion.
