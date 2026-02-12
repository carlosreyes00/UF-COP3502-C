print("""Available movies today:
A)12 Strong:   1)2:30  2)4:40 3)7:50 4)10:50
B)Coco:        1)12:40 2)3:45
C)The Post:    1)12:45 2)3:35 3)7:05 4)9:55""")

adultBefore2PM = 11.17
adultAfter2PM = 12.45
childBefore2PM = 8.00
childAfter2PM = 9.68

def ask_for_amount_of_tickets(showtime) -> float:
    adult_tickets = int(input("Adult tickets: "))
    if adult_tickets <= 30:
        kid_tickets = int(input("Kid tickets: "))
        if adult_tickets + kid_tickets <= 30:
            adult_price = adultBefore2PM if showtime == "before" else adultAfter2PM
            kid_price = childBefore2PM if showtime == "before" else childAfter2PM
            total_cost = adult_tickets * adult_price + kid_tickets * kid_price
            return total_cost
        else:
            return -1 # invalid input signal
    else:
        return -1 # invalid input signal

movieChoice = input("Movie choice: ")
if movieChoice == "A":
    showTime = input("Showtime: ")
    if showTime == "1" or showTime == "2" or showTime == "3" or showTime == "4":
        totalCost = ask_for_amount_of_tickets("after")
        if totalCost == -1:
            print("Invalid option; please restart app...")
        else:
            print(f"Total cost: ${totalCost:.2f}")
    else:
        print("Invalid option; please restart app...")
elif movieChoice == "B":
    showTime = input("Showtime: ")
    if showTime == "1":
        totalCost = ask_for_amount_of_tickets("before")
        if totalCost == -1:
            print("Invalid option; please restart app...")
        else:
            print(f"Total cost: ${totalCost:.2f}")
    elif showTime == "2":
        totalCost = ask_for_amount_of_tickets("after")
        if totalCost == -1:
            print("Invalid option; please restart app...")
        else:
            print(f"Total cost: ${totalCost:.2f}")
    else:
        print("Invalid option; please restart app...")
elif movieChoice == "C":
    showTime = input("Showtime: ")
    if showTime == "1":
        totalCost = ask_for_amount_of_tickets("before")
        if totalCost == -1:
            print("Invalid option; please restart app...")
        else:
            print(f"Total cost: ${totalCost:.2f}")
    elif showTime == "2" or showTime == "3" or showTime == "4":
        totalCost = ask_for_amount_of_tickets("after")
        if totalCost == -1:
            print("Invalid option; please restart app...")
        else:
            print(f"Total cost: ${totalCost:.2f}")
    else:
        print("Invalid option; please restart app...")
else:
        print("Invalid option; please restart app...")