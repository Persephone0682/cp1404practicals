sales = float(input("Sales: "))
if sales < 1000:
    bonus = sales * 0.10
else:
    bonus = sales * 0.15
print(f"Your bonus is: 4{bonus:.2f}")