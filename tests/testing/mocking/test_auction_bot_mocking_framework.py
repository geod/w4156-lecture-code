import unittest
from unittest.mock import MagicMock
from lectures.testing.mocking.auction_bot import AuctionBot, Quote, AcmeOrderEntryConnector, Order


class AuctionBotTestCase(unittest.TestCase):
    """
    This is the same as the example 'test_auction_bot'. However, in this example I save myself having
    to write a MockConnector by using mocking frameworks. The python mocking framework provides super handy
    objects which can behave very flexibly as mock objects
    https://docs.python.org/3/library/unittest.mock.html
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
