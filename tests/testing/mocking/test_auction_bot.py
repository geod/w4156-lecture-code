import unittest
import logging
from lectures.testing.mocking.auction_bot import AuctionBot, Quote, Order

logging.getLogger().setLevel(logging.DEBUG)


class MockConnector:
    """
    There are various python helpers for this. However, lets write an actual mock class ourselves just to make
    it blatantly obvious what is happening.

    We can then use the various python helpers (magic mock) to do the same without having to write my own mock instances
    of various objects (in this instance writing a mock connector is boring and tedious). This is why mocking frameworks
    exist.
    """
    def __init__(self):
        self.i_was_called_with = []

    def submit_order(self, order: Order):
        logging.debug("Mock Connector was called with:%s" % (order))
        self.i_was_called_with.append(order)
        return True

    def number_calls(self):
        return len(self.i_was_called_with)

    def pop(self):
        return self.i_was_called_with.pop()

    def reset(self):
        self.i_was_called_with.clear()


class AuctionBotTestCase(unittest.TestCase):
    """
    Remember there are three components
    A) the feed (gets prices)
    B) the auction bot (the business logic)
    C) the order connector (sends orders to the auction venue)

    Lets say I want to focus on testing the auction bot business logic
    1. I DO NOT need to mock the feed connector (because the auction bot does not have a reference to it
    2. However, the auction bot does know about the connector. Therefore, I need to mock it out to test the auction
    bot in isolation

    When I do this I have
    AuctionBot -> MockConnector

    In this test I:
    Push in values -> AuctionBot -> Capture What AuctionBot asked the connector to do
    """
    def setUp(self):
        self.mock_connector = MockConnector()

        # we then create a normal auction bot. We pass it a mock connector
        self.auction_bot = AuctionBot(self.mock_connector, 10)

    def assertOrder(self, side: Order.SIDE, price: int, quantity: int):
        """
        Helper method to assert the mock was called with appropriate values
        :param side:
        :param price:
        :param quantity:
        :return:
        """
        self.assertEqual(self.mock_connector.number_calls(), 1)
        submitted_order: Order = self.mock_connector.pop()
        self.assertEqual(submitted_order.side, side)
        self.assertEqual(submitted_order.price, price)
        self.assertEqual(submitted_order.quantity, quantity)
        self.mock_connector.reset()

    def assertNoCall(self):
        self.assertEqual(self.mock_connector.number_calls(), 0)

    def test_auction_bot(self):
        # I am pushing in a dummy quote
        self.auction_bot.on_price_change(Quote(5))

        # I expect that the auction bot submitted an order so I assert
        self.assertOrder(Order.SIDE.BUY, 6, 1)

        # If the quote remains 5 then nothing should be submitted / change
        self.auction_bot.on_price_change(Quote(5))
        self.assertNoCall()

        self.auction_bot.on_price_change(Quote(6))
        self.assertNoCall()

        self.auction_bot.on_price_change(Quote(7))
        self.assertOrder(Order.SIDE.BUY, 8, 1)

        self.auction_bot.on_price_change(Quote(9))
        self.assertOrder(Order.SIDE.BUY, 10, 1)

        self.auction_bot.on_price_change(Quote(10))
        self.assertNoCall()

        self.auction_bot.on_price_change(Quote(11))
        self.assertNoCall()

        # I would expect that the bot calls the connector


if __name__ == '__main__':
    unittest.main()
