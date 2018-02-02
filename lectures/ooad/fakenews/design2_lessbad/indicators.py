from abc import ABC, abstractmethod
import requests
import whois
import datetime
from statistics import mean


class AbstractDomainScorer(ABC):

    @abstractmethod
    def score_domain(self, newsurl):
        pass


class WhitelistScorer(AbstractDomainScorer):

    def __init__(self, filename):
        self.__whitelist = {}
        with open('whitelist.txt') as f:
            entry = f.readline()
            domain, score = entry.split(",")[0], [1]
            self.__whitelist[domain] = score

    def score_domain(self, newsurl):
        whitelist_score = 0.5
        whitelist_score = self.__whitelist.get(newsurl, whitelist_score)


class ContentScorer(AbstractDomainScorer):

    def __init__(self):
        self.__keywords = []
        with open('keywords.txt') as f:
            kw = f.readline()
            self.__keywords.append(kw)

    def score_domain(self, newsurl):
        content_score = 0.5
        r = requests.get(newsurl)
        if r.status_code == 200:
            for keyword in self.__keywords:
                if keyword in r.text:
                    content_score = max(content_score - 0.1, 0)


class WhoisScorer(AbstractDomainScorer):

    def score_domain(self, newsurl):
        domain_score = 0.5
        domain = whois.query(newsurl)
        if domain is not None:
            daysalive = (datetime.datetime.now() - domain.creation_date).days
            # 0 days is 0, 365 is 0.5, 730 is 1
            domain_score = min(daysalive, 730) / 730
