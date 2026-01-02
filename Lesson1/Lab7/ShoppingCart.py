cart = [] 

for i in range(5):
    item = input(f"Enter an item in the cart {i+1}: ")
    cart.append(item)

print("Final items in the cart : ", cart)

remove_cart = cart.pop()
print("Removed the last item in the cart : ",remove_cart)

print("Remaining items in the cart is: ",len(cart))

if len(cart) > 0:
    print("First item in the cart is:", cart[0])
    print("Last item in the cart is:", cart[-1])
else:
    print("Cart is empty!")

