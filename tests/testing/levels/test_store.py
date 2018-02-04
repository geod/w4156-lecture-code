import unittest


class TestStore(unittest.TestCase):

    def setUp(self):
        """
        You may want to create an inventory, till, store and inject the inventory and till into the store
        In pseudeo code
        i = Inventory()
        t = CashRegister()
        s = Store()
        s.till = t
        s.inventory = i
        self.store = s
        """
        pass

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
