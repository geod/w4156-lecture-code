from abc import ABC, abstractmethod
import csv
import requests
import whois
from datetime import date
from statistics import mean
from bs4 import BeautifulSoup


class AbstractDomainScorer(ABC):

    @abstractmethod
    def score_domain(self, newsurl):
        pass


class WhitelistScorer(AbstractDomainScorer):

    def __init__(self, baseconfigdir=".", filename='whitelist.csv'):
        self.__whitelist = {}
        with open(baseconfigdir + "/" + filename) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                self.__whitelist[row[0].lower()] = float(row[1])

    def score_domain(self, newsurl):
        if newsurl is None:
            raise ValueError('Requires valid URL')
        whitelist_score = 0.5
        whitelist_score = self.__whitelist.get(newsurl.lower(), whitelist_score)
        return whitelist_score


class ContentScorer(AbstractDomainScorer):

    def __init__(self, baseconfigdir=".", filename='keywords.csv'):
        self.__keywords = []
        with open(baseconfigdir + "/" + filename) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                self.__keywords.append(row[0])

    def score_domain(self, newsurl):
        content_score = 0.5
        r = requests.get(newsurl)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text)
            text = soup.get_text().lower()
            for keyword in self.__keywords:
                if keyword in text:
                    content_score = max(content_score - 0.1, 0)
        return content_score


class WhoisScorer(AbstractDomainScorer):

    def score_domain(self, newsurl):
        domain_score = 0.5
        domain = whois.query(newsurl)
        if domain is not None:
            today = date.today()
            daysalive = (today - domain.creation_date)
            # 0 days is 0, 365 is 0.5, 730 is 1
            domain_score = min(max(0,daysalive.days), 730) / 730
        return domain_score


class AggregateScorer(AbstractDomainScorer):

    def __init__(self):
        self.__scorers = []

    def add_scorer(self, scorer: AbstractDomainScorer):
        if scorer in self.__scorers:
            raise ValueError("Duplicate Scorer")
        self.__scorers.append(scorer)

    def score_domain(self, newsurl):
        scores = []
        for scorer in self.__scorers:
            scores.append(scorer.score_domain(newsurl))
        res = mean(scores)
        return res


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

