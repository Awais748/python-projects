menu = {
    "popcorn": 3.00,
    "soda": 4.50,
    "nachos": 2.50,
    "candy": 1.00,
    "fries": 3.25,
    "lemonade": 4.25
}
cart = []
total = 0

print("\n----- MENU -----")
for key, value in menu.items():
    print(f"{key:10} - ${value:.2f}")
print("-----------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print(f"{food} added to cart!")
    else:
        print("Item not available. Try again!")

print("\n----- YOUR CART -----")
for item in cart:
    total += menu[item]
    print(f"{item} - ${menu[item]:.2f}")

print(f"\nTotal is: ${total:.2f}")