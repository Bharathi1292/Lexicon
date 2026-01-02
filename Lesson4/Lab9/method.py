class Product:
    def __init__(self, price):
        self.price = price  

    def discounted_price(self, percent):
        return self.price * (1 - percent / 100) 

product = Product(100)
print(f"Original price: ${product.price}")
print(f"Price after 10% discount: {product.discounted_price(10)}")

product.price = 150
print("\nAfter changing the price:")
print(f"Original price: {product.price}")
print(f"Price after 10% discount: {product.discounted_price(10)}")

