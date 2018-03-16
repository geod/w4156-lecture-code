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

    def __init__(self, filename='whitelist.csv'):
        self.__whitelist = {}
        with open(filename) as csvfile:
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

    def __init__(self, filename='keywords.csv'):
        self.__keywords = []
        with open(filename) as csvfile:
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
