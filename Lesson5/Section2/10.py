class ShoppingCart:
    def __init__(self, **items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return "\n".join([f"{item}: {qty}" for item, qty in self.items.items()])

cart = ShoppingCart(apple=3, banana=2, orange=5)

print("banana" in cart)  
print("grape" in cart)  
