side1 = float(input("Side length 1: "))
side2 = float(input("Side length 2: "))
side3 = float(input("Side length 3: "))

if side1 == side2 and side2 == side3:
    print("This is an equilateral triangle!")
elif side1 != side2 and side2 != side3 and side1 != side3:
    print("This is a scalene triangle!")
else:
    print("This is an isosceles triangle!")