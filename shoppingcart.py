products = []
prices = []
total = 0
while True:
    product = input("Enter a food to buy (q to quit):") 
    if product.lower() == "q":
       break 
    else:
        price = float(input(f"Enter the price of a {product}: $"))
        products.append(product)
        prices.append(price)

print("\n----- YOUR CART -----")
total = 0

for i in range(len(products)):
    print(f"{products[i]} - ${prices[i]}")
    total += prices[i]
print(f"\nYour total is: ${total}")
print("Thanks for shopping with us!")