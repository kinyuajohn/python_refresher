print("----------------------------------------------")
# --------------------- shopping cart ---------------------
# ---------------------------------------------------------
foods = []
prices = []
count = 0
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q" or food == "":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n----- YOUR CART -----")

for food in foods:
    count += 1
    print(f"{count}. {food} ", end=" ")

for price in prices:
    price += price

print()
print(f"Your total is ${price:.2f}")
