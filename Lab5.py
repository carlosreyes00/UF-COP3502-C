
def print_menu():
    print('''Decoding Menu
-------------
1. Decode hexadecimal
2. Decode binary
3. Convert binary to hexadecimal
4. Quit\n''')

# Decodes a single hexadecimal digit and returns its decimal value.
def hex_char_decode(digit):
    if digit.isnumeric() and 0 <= int(digit) < 16:
        return digit
    else:
        if digit == "A" or digit == "a":
            return 10
        elif digit == "B" or digit == "b":
            return 11
        elif digit == "C" or digit == "c":
            return 12
        elif digit == "D" or digit == "d":
            return 13
        elif digit == "E" or digit == "e":
            return 14
        elif digit == "F" or digit == "f":
            return 15
        else:
            return -1

def dec_digit_to_hex(digit):
    digit = int(digit)
    if 0 <= digit < 10:
        return str(digit)
    else:
        if digit == 10:
            return "A"
        elif digit == 11:
            return "B"
        elif digit == 12:
            return "C"
        elif digit == 13:
            return "D"
        elif digit == 14:
            return "E"
        elif digit == 15:
            return "F"
        else:
            return -1

# Decodes an entire hexadecimal string and returns its decimal value.
def hex_string_decode(hex):
    if hex[:2] == "0x" or hex[:2] == "0X":
        hex = hex[2:len(hex)]

    result = 0
    index = 0

    for i in hex:
        result += int(hex_char_decode(i)) * 16 ** (len(hex)-index-1)
        index += 1

    return result

# Decodes a binary string and returns its decimal value.
def binary_string_decode(binary):
    if binary[:2] == "0b" or binary[:2] == "0B":
        binary = binary[2:len(binary)]

    result = 0
    index = 0

    for i in binary:
        result += int(i) * 2 ** (len(binary)-index-1)
        index += 1

    return result

# Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string.
def binary_to_hex(binary):
    decimal = binary_string_decode(binary)
    hexadecimal = ""
    while decimal > 0:
        if decimal < 16:
            hexadecimal = dec_digit_to_hex(decimal) + str(hexadecimal)
            return hexadecimal
        else:
            hexadecimal = dec_digit_to_hex(decimal%16) + hexadecimal
            decimal //= 16

    print("result:", hexadecimal)
    return hexadecimal

while True:
    print_menu()
    option = int(input("Please enter an option: "))

    if option == 1:
        user_input = input("Please enter the numeric string to convert: ")
        result = hex_string_decode(user_input)
        print(f"Result: {result}\n")
    elif option == 2:
        user_input = input("Please enter the numeric string to convert: ")
        result = binary_string_decode(user_input)
        print(f"Result: {result}\n")
    elif option == 3:
        user_input = input("Please enter the numeric string to convert: ")
        result = binary_to_hex(user_input)
        print(f"Result: {result}\n")
    elif option == 4:
        print("Goodbye!")
        break
    else:
        break