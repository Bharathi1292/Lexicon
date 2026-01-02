class ShoppingCart:
    def __init__(self, **items):
        self.items = items

    def __len__(self):
        return sum(self.items.values())

    def __str__(self):
        return "\n".join([f"{item}: {qty}" for item, qty in self.items.items()])

cart = ShoppingCart(apple=3, banana=2, orange=5)

print(cart)          
print("Total items:", len(cart))  
