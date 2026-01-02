class ShoppingCart:
    def __init__(self, **items):
        self.items = items

    def __getitem__(self, item):
        if item in self.items:
            return self.items[item]
        else:
            raise KeyError(f"{item} not found in the cart")

    def __str__(self):
        return "\n".join([f"{item}: {qty}" for item, qty in self.items.items()])

cart = ShoppingCart(apple=3, banana=2, orange=5)

print(cart["apple"])  
print(cart["orange"])  
# print(cart["grape"])
