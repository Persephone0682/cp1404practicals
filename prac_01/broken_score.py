score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score > 50:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("Bad")