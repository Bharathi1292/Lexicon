class ShoppingCart:
    def __init__(self, **items):
        self.items = items

    def __add__(self, other):
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        combined_items = self.items.copy()
        for item, qty in other.items.items():
            if item in combined_items:
                combined_items[item] += qty
            else:
                combined_items[item] = qty
        return ShoppingCart(**combined_items)

    def __str__(self):
        return "\n".join([f"{item}: {qty}" for item, qty in self.items.items()])

cart1 = ShoppingCart(apple=3, banana=2)
cart2 = ShoppingCart(banana=1, orange=5)
combined_cart = cart1 + cart2
print(combined_cart)
