import math

currentResult = 0
sumOfCalculations = 0
numberOfCalculations = 0

print(f"Current Result: {currentResult:.1f}\n")

menu = """Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average\n"""

print(menu)

while(True):

    operation = int(input("Enter Menu Selection: "))

    if operation == 0:
        break
    elif operation == 1:
        operand1 = input("Enter first operand: ")
        operand1 = currentResult if operand1 == "RESULT" else float(operand1)
        operand2 = input("Enter second operand: ")
        operand2 = currentResult if operand2 == "RESULT" else float(operand2)
        currentResult = operand1 + operand2
        print(f"Current Result: {currentResult}\n")
        print(menu)
        sumOfCalculations += currentResult
        numberOfCalculations += 1
    elif operation == 2:
        operand1 = input("Enter first operand: ")
        operand1 = currentResult if operand1 == "RESULT" else float(operand1)
        operand2 = input("Enter second operand: ")
        operand2 = currentResult if operand2 == "RESULT" else float(operand2)
        currentResult = operand1 - operand2
        print(f"Current Result: {currentResult}\n")
        print(menu)
        sumOfCalculations += currentResult
        numberOfCalculations += 1
    elif operation == 3:
        operand1 = input("Enter first operand: ")
        operand1 = currentResult if operand1 == "RESULT" else float(operand1)
        operand2 = input("Enter second operand: ")
        operand2 = currentResult if operand2 == "RESULT" else float(operand2)
        currentResult = operand1 * operand2
        print(f"Current Result: {currentResult}\n")
        print(menu)
        sumOfCalculations += currentResult
        numberOfCalculations += 1
    elif operation == 4:
        operand1 = input("Enter first operand: ")
        operand1 = currentResult if operand1 == "RESULT" else float(operand1)
        operand2 = input("Enter second operand: ")
        operand2 = currentResult if operand2 == "RESULT" else float(operand2)
        currentResult = operand1 / operand2
        print(f"Current Result: {currentResult}\n")
        print(menu)
        sumOfCalculations += currentResult
        numberOfCalculations += 1
    elif operation == 5:
        operand1 = input("Enter first operand: ")
        operand1 = currentResult if operand1 == "RESULT" else float(operand1)
        operand2 = input("Enter second operand: ")
        operand2 = currentResult if operand2 == "RESULT" else float(operand2)
        currentResult = operand1 ** operand2
        print(f"Current Result: {currentResult}\n")
        print(menu)
        sumOfCalculations += currentResult
        numberOfCalculations += 1
    elif operation == 6:
        operand1 = input("Enter first operand: ")
        operand1 = currentResult if operand1 == "RESULT" else float(operand1)
        operand2 = input("Enter second operand: ")
        operand2 = currentResult if operand2 == "RESULT" else float(operand2)
        currentResult = math.log(operand2, operand1)
        print(f"Current Result: {currentResult}\n")
        print(menu)
        sumOfCalculations += currentResult
        numberOfCalculations += 1
    elif operation == 7:
        if currentResult != 0:
            print(f"Sum of calculations: {sumOfCalculations:.2f}")
            print(f"Number of calculations: {numberOfCalculations}")
            print(f"Average of calculations: {(sumOfCalculations/numberOfCalculations):.2f}\n")
        else:
            print("Error: No calculations yet to average!\n")
    else:
        print("Error: Invalid selection!\n")

print("Thanks for using this calculator. Goodbye!")
