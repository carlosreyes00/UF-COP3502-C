income = float(input("Enter your total income this year: "))

taxes = 0

if income > 0:
    taxes += min(income, 11600) * 0.1
    income -= 11600

if income > 0:
    taxes += min(income, 47150-11600) * 0.12
    income -= 47150-11600

if income > 0:
    taxes += min(income, 100525-47150) * 0.22
    income -= 100525-47150

if income > 0:
    taxes += min(income, 191950-100525) * 0.24
    income -= 191950-100525

if income > 0:
    taxes += min(income, 243725-191950) * 0.32
    income -= 243725-191950

if income > 0:
    taxes += min(income, 609350-243725) * 0.35
    income -= 609350-243725

if income > 0:
    taxes += income * 0.37

print(f"You owe ${taxes:.2f} this year.")