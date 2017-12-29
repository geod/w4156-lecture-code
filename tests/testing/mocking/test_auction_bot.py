import unittest
from unittest.mock import MagicMock

from lectures.testing.mocking.auction_bot import AuctionBot, Quote, AcmeOrderEntryConnector, Order


class AuctionBotTestCase(unittest.TestCase):
    """
    Remember there are three components
    A) the feed (gets prices)
    B) the auction bot (the business logic)
    C) the order connector


    The challenge with testing the OVERALL auction bot is
    1. It connects to something external (that we may not have the code of and control)
    2. We want to test the individual units of our program independently

    Let's say in this test case we want to focus on testing the auction bot business logic.
    How can we test that independently of the feed, the order connector or the external exchange?
    """

    def setUp(self):
        # We create an instance of connector
        connector = AcmeOrderEntryConnector("foo")

        # but importantly we create a mock object
        self.mock_submit = MagicMock(return_value=True)

        # and override the submit_order method to be a mock
        # This means whenever someone calls 'submit_order' they hit our mock and not the real connector
        connector.submit_order = self.mock_submit

        # we then create a normal auction bot. The connector that we pass has the submit_order method mocked
        self.auction_bot = AuctionBot(connector, 10)

    def assertOrder(self, side: Order.SIDE, price: int, quantity: int):
        """
        Helper method to assert the mock was called with appropriate values
        :param side:
        :param price:
        :param quantity:
        :return:
        """
        self.mock_submit.assert_called_once()
        submitted_order: Order = self.mock_submit.call_args[0][0]
        self.assertEqual(submitted_order.side, side)
        self.assertEqual(submitted_order.price, price)
        self.assertEqual(submitted_order.quantity, quantity)
        self.mock_submit.reset_mock()

    def assertNoCall(self):
        self.mock_submit.assert_not_called()

    def test_auction_bot(self):
        # I am pushing in a dummy quote
        self.auction_bot.on_price_change(Quote(5))

        # I expect that the auction bot submitted an order so I assert
        self.assertOrder(Order.SIDE.BUY, 6, 1)

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
