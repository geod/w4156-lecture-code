from collections import namedtuple
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

"""
DISCLAIMER - I have written the ugliest procedural version of the problem I can muster.
If you were looking for the 'good code' examples you took a wrong turn!!!!
"""

# as close as I can get to structs in python
Item = namedtuple('Item', 'sku, name, price')

# how many we have of those things
inventory = []

# how much cash we have
cash = 0

def browse():
    unique_items = {}
    for item in inventory:
        unique_items[item.sku] = item
    return unique_items


def buy(sku, quantity):
    global inventory
    matching_items = list(filter(lambda x: x.sku is sku, inventory))
    if(len(matching_items) < quantity):
        raise Exception("Not enough to sell")
    else:
        purchases = inventory[0:quantity]
        inventory = inventory[quantity:len(inventory)]
        global cash
        for p in purchases:
            cash += p.price
        return quantity


def refund(item):
    global cash
    cash -= item.price
    inventory.append(item)


def restock(item):
    logging.info("Restock:%s", item)
    inventory.append(item)


def reprice(sku, new_price):
    for i in inventory:
        if i.sku is sku:
            i.price = new_price

if __name__ == '__main__':
    """
    lets go shopping
    """

    i1 = Item(sku="AB1123", name="Hot Sauce", price=1.99)
    i2 = Item(sku="AB1123", name="Hot Sauce", price=1.99)
    i3 = Item(sku="AB1124", name="Pringles", price=3.99)
    restock(i1)
    restock(i2)
    restock(i3)

    can_buy = browse()
    logging.info("Found %s Unique Items", len(can_buy))

    buy("AB1124", 1)

    logging.info("Inventory Size: %s", len(inventory))
    logging.info("Cash : %s", cash)

    buy("AB1123", 1)

    logging.info("Inventory Size: %s", len(inventory))
    logging.info("Cash : %s", cash)

    i3 = Item(sku="AB1125", name="Chocolate", price=5.60)
    refund(i3)

    logging.info("Inventory Size: %s", len(inventory))
    logging.info("Cash : %s", cash)


"""
UC-1: people can browse
UC-2: attempt to buy things
    UC-2a: enough money
    UC-2b: not enough
UC-3: return/refund
UC-5: restock
UC-6: reprice item
    UC-6a: single item (bashed)
    UC-6b: all items
"""

