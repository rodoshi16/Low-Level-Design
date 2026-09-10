**Law_of_demeter**

You have:

A Customer who owns a ShoppingCart
The cart contains a list of CartItems
Each CartItem refers to a Product
And every Product has a Price
Now let’s say you want to display the price of the first product in a customer’s shopping cart.

customer.get_shopping_cart.get_items[0].get_product().get_price()

*This is wrong - why?*

1. If shoppingcart changes, cr how it stores items or cartItem gets renamed or pricing is stored differently - orderService code breaks

2. Encapsulation violation - customer exposes its shopping cart exposes items etc

3. Tesability - to test this one method you need to mock all involved objects

**Law of demeter - only talk to your immediate friends**

A should not be able to reach C through B, only B can get info about C. 

Refactoring:

```
class ShoppingCart:
    def __init__(self):
        self._items = []

    # ... other methods ...

    def get_first_item_price(self):
        if not self._items:
            return Money.ZERO
        return self._items[0].get_product().get_price()
```

Notice that ShoppingCart still reaches into CartItem and Product. That is fine here because ShoppingCart owns the items. The chain stays within the cart's own responsibility boundary. The important thing is that external callers no longer need to know about these internals.

```
class Customer:
    def __init__(self, shopping_cart):
        self._shopping_cart = shopping_cart

    # ... other methods ...

    def get_first_cart_item_price(self):
        return self._shopping_cart.get_first_item_price()
```