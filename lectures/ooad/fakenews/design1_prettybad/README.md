## Object Oriented Analysis

### Identifying missing concepts

Ok - so the first thing we do is recognize there is a missing concept which was something
which scores a domain. I have three of these 'things'
1. Something which scores using a whitelist
2. Something which scores using content
3. Something which scores using DNS record age

Let's therefore create an abstract class called domain scorer!

```python
class AbstractDomainScorer(ABC):

    @abstractmethod
    def score_domain(self, newsurl):
        """
        Provides a score for the trustworthyness of a domain
        :param newsurl:
        :return: a score for the trustworthyness between 0 and 1 where 1 is fully trustworthy and 0 is nonsense
        """
        pass
```

And then refactor the 'blob' of code that was whitelist into it's own class which extends AbstractDomainScorer
```python
class WhitelistScorer(AbstractDomainScorer):
    """
    Whitelist scorer scores on whether the domain is in a preconfigured whitelist
    """

    def __init__(self, filename):
        self.__whitelist = {}
        with open('whitelist.txt') as f:
            entry = f.readline()
            domain, score = entry.split(",")[0], [1]
            self.__whitelist[domain] = score

    def score_domain(self, newsurl):
        whitelist_score = 0.5
        whitelist_score = self.__whitelist.get(newsurl, whitelist_score)

```

My flask service now looks a little better

```python
@app.route('/fakenews')
def score_url():
    newsurl = request.args.get('newsurl')
    content_score = content_scorer.score_domain(newsurl)
    whitelist_score = whitelist_scorer.score_domain(newsurl)
    whois_score = whois_scorer.score_domain(newsurl)

    score = content_score + whitelist_score + whois_score / 3
    return json({'score': score})
```

### Am I happy?
Nope - still not happy:

##### fixed issues

1. It is hard to test the scoring logic outside of flask
2. It is hard to test individual scoring logic (whitelist, content, domain) independent of each other
3. We do not associate data (whitelist and content keywords) with the function (the former is at the top, the latter is at the bottom)

##### partially fixed
4. There is a growing 'blob' of code within the handler. Right now it is almost readable but wont become readable if I add more scorers or make any one of them more complex

##### not fixed
5. Not super easy to add a new scorer
6. Not super easy to change the weighting of different scorers
7. The webservice just knows too much. All it needs to know is there is something which scores a domain. We do not need to expose the messiness
