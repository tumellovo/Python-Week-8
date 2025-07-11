#Shopping cart program

foods = []
prices = []
total = 0

while True :
    food = input("Enter item name (press q to quit): ")
    if food.lower() == "q":
      break
    else:
      price = float(input(f"Enter price of {food}: R"))
      foods.append(food)
      prices.append(price)
      
print("----YOUR CART----")

for food in foods:
    print(food)
    
for price in prices:
    total += price
    
print()
print(f"Your total is: R{total}")       