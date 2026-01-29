unitFrom = input("Enter the unit you are converting from: ")
unitTo = input("Enter the unit you are converting to: ")
temperature = float(input(f"Enter the temperature in {unitFrom}: "))

result = 0

if unitFrom == unitTo:
    print(f"That is {temperature:.1f} degrees {unitTo}.")
else:
    if unitFrom == "Fahrenheit":
        if unitTo == "Celsius":
            result = (temperature - 32) * 5/9
        else:
            result = (temperature - 32) * 5/9 + 273.15
    elif unitFrom == "Celsius":
        if unitTo == "Fahrenheit":
            result = (temperature * 9/5) + 32
        else:
            result = temperature + 273.15
    else:
        if unitTo == "Celsius":
            result = temperature - 273.15
        else:
            result = (temperature - 273.15) * 9/5 + 32

    print(f"That is {result:.1f} degrees {unitTo}.")