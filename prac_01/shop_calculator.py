TOTAL = 0.0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
for i in range(items):
    price = float(input("Price of item: "))
    TOTAL += price
if TOTAL >100:
    TOTAL *= 0.9
print(f"Total price for {items} items is ${TOTAL:.2f}")