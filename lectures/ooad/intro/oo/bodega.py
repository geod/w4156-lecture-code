from collections import defaultdict

"""
Admittedly - this is not a direct translation of the procedural version (this one is richer functionality)
"""

class Product:
    """
    A product is a thing we sell
    """

    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price


class ProductCatalogue:
    """
    Product catalogue defines the 'list of things' we sell
    If it is not in the product catalogue we do not sell it!
    """

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.sku] = product

    def get_product(self, sku):
        return self.products[sku]

    def contains(self, product):
        return self.products[product.sku] is not None

class InventoryItem:

    def __init__(self, product: Product, item_price=None):
        self.item_price = item_price # None unless item has a specific price
        self.product = product

    def price(self):
        """
        The price is the product price unless this individual item has been marked down/up
        :return:
        """
        purchase_price = self.product.price
        if self.item_price is not None:
            purchase_price = self.item_price
        return purchase_price


class Inventory:

    def __init__(self):
        self.product_catalogue = ProductCatalogue()
        self.inventory = defaultdict(list)

    def add_item(self, item: InventoryItem):

        self.inventory[item.sku].append(item)


class Register:

    def __init__(self, cash=1000):
        self.cash = cash

    def ring_up(self, inventory_item):
        self.cash += inventory_item.price()

    def refund(self, inventory_item):
        self.cash -= inventory_item.price()

class Bodega:

    def __init__(self):
        self.register = Register()
        self.inventory = Inventory()

    def stock(self, item):
        self.inventory.add_item(item)

    def browse(self):
        return self.inventory.items()

    def refund(self, item):
        self.inventory.add_item(item)
        self.register.refund(item)

    def purchase(self, product, quantity):
        if self.inventory.has(product, quantity):
            item = self.inventory.remove(product, quantity)
            self.register.ring_up(item)
            return item
        else:
            raise Exception("We dont have what you want")


if __name__ == '__main__':
    b = Bodega()

    chips = Product("AS1231", "Chips", 0.99)
    i1 = InventoryItem(chips)
    i2 = InventoryItem(chips)







