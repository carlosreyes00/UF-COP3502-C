
itemPrice = float(input("Enter the price of the item: "))
taxPercentage = float(input("Enter the sales tax percentage: "))

itemPrice += itemPrice * taxPercentage / 100

print(f"Your total is ${itemPrice:.2f}")
