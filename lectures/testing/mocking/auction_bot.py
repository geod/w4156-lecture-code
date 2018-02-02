import requests
import abc
from abc import ABC
from enum import Enum, auto
import logging
import time


class Order:
    class SIDE(Enum):
        BUY = 1
        SELL = -1

    def __init__(self, side: SIDE, price: int, quantity: int):
        self.side = side
        self.price = price
        self.quantity = quantity


class OrderConnector(ABC):

    @abc.abstractmethod
    def submit_order(self, order: Order) -> bool:
        """

        :param order:
        :return:
        """


class Quote:

    def __init__(self, offer):
        self.offer = offer


class PriceListener(ABC):

    @abc.abstractmethod
    def on_price_change(self, quote: Quote):
        """

        :param data:
        :return:
        """


class AcmePriceFeedConnector:

    def __init__(self, url_path: str, listener: PriceListener):
        self._url_path = url_path
        self._keep_running = True
        self._listener = listener

    def set_keep_running(self, run):
        self.keep_running = run

    def run(self):
        while self.keep_running:
            try:
                data = requests.get(self.url_path).json()
                q = Quote(data.offer)
                self._listener.on_price_change(q)
            except Exception:
                logging.warning("Exception while polling")
            time.sleep(1)

    temperature = property(set_keep_running)


class AuctionBot(PriceListener):

    def __init__(self, conn: OrderConnector, max_price: int):
        self._connector = conn
        self._max_price = max_price
        self._my_bid = 0

    def on_price_change(self, quote: Quote):
        # dont outbid ourselves
        if quote.offer > self._my_bid:

            snipe_bid_px = quote.offer + 1
            if snipe_bid_px <= self._max_price:
                o = Order(Order.SIDE.BUY, snipe_bid_px, 1)
                success = self._connector.submit_order(o)
                self._my_bid = snipe_bid_px if success else None


class AcmeOrderEntryConnector(OrderConnector):

    def __init__(self, url: str):
        self._url = url

    def submit_order(self, order: Order):
        data = {'side': order.side, 'price': order.price, 'quantity': order.quantity}
        r = requests.post(self._url + '/order', data)
        return r.status_code == requests.codes.ok


"""
The code would be used something like this
url = "http://localhost:5006"
connector = AcmeOrderEntryConnector(url)
bot = AuctionBot(connector, 15, 18)
feed = AcmePriceFeedConnector(url, bot)
feed.run()
"""


