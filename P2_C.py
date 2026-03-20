def dec_digit_to_hex(digit):
    digit = int(digit)
    if 0 <= digit < 10:
        return str(digit)
    else:
        if digit == 10:
            return "a"
        elif digit == 11:
            return "b"
        elif digit == 12:
            return "c"
        elif digit == 13:
            return "d"
        elif digit == 14:
            return "e"
        elif digit == 15:
            return "f"
        else:
            return -1

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

# Ex: to_hex_string([3,15,6,4]) returns the string '3f64'
def to_hex_string(data):
    result = ""
    for i in range(len(data)):
        result += dec_digit_to_hex(data[i])
    return result

# Ex: count_runs([15,15,15,4,4,4,4,4,4]) returns the int 2
def count_runs(flat_data):
    result = 1
    count = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] != flat_data[i-1]:
            result += 1
            count = 0
        else:
            count += 1
            if count == 15:
                count = 0
                result += 1
    return result

# Ex: encode_rle([15,15,15,4,4,4,4,4,4]) returns the list of ints [3,15,6,4]
def encode_rle(flat_data):
    result = []
    count = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] != flat_data[i - 1]:
            result.append(count)
            result.append(flat_data[i-1])
            count = 1
        else:
            count += 1
            if count == 15:
                result.append(count)
                result.append(flat_data[i - 1])
                count = 0
    result.append(count)
    result.append(flat_data[i])
    return result

# Ex: get_decoded_length([3,15,6,4]) returns the int 9
def get_decoded_length(rle_data):
    result = 0
    for i in range(0,len(rle_data),2):
        result += rle_data[i]
    return result

# Ex: decode_rle([3,15,6,4]) returns the list of ints [15,15,15,4,4,4,4,4,4]
def decode_rle(rle_data):
    result = []
    for i in range(0, len(rle_data), 2):
        for j in range(0, rle_data[i]):
            result.append(rle_data[i+1])
    return result

# Ex: string_to_data('3f64') returns the list of ints [3,15,6,4]
def string_to_data(data_string):
    result = []
    for i in range(len(data_string)):
        result.append(int(hex_char_decode(data_string[i])))
    return result

# Ex: to_rle_string([15,15,6,4]) returns the string '15f:64'
def to_rle_string(rle_data):
    result = ""
    for i, item in enumerate(rle_data):
        if i % 2 == 0:
            result += str(item)
        else:
            result += dec_digit_to_hex(item) + ":"

    result = result[0:len(result)-1]

    return result

# Ex: string_to_rle('15f:64') returns the list of ints [15,15,6,4]
def string_to_rle(rle_string):
    result = []
    string_splitted = rle_string.split(":")

    for item in string_splitted:
        if len(item) == 2:
            result.append(int(item[0]))
            result.append(int(hex_char_decode(item[1])))
        elif len(item) == 3:
            result.append(int(item[0:2]))
            result.append(int(hex_char_decode(item[2])))

    return result

import console_gfx


def print_menu():
    print('''\nRLE Menu
--------
0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data\n''')

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    print()

    while True:
        print_menu()
        user_option = int(input("Select a Menu Option:"))

        if user_option == 0:
            break
        elif user_option == 1:
            file_to_load = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(file_to_load)
        elif user_option == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif user_option == 3:
            rle_string = input("Enter an RLE string to be decoded:")
        elif user_option == 4:
            rle_hex_string = input("Enter the hex string holding RLE data:")
        elif user_option == 5:
            flat_data = input("Enter the hex string holding flat data:")
        elif user_option == 6:
            print("Displaying image...")
            console_gfx.display_image(image_data)
        elif user_option == 7:
            print("RLE representation:", to_rle_string(string_to_data(rle_hex_string)))
        elif user_option == 8:
            print("RLE hex values:", to_hex_string(string_to_rle(rle_string)))
        elif user_option == 9:
            aux = decode_rle(string_to_rle(rle_string))
            result = ""
            for item in aux:
                result += str(item)
            print("Flat hex values:", result)

if __name__ == "__main__":
    main()

    """
    3
    19:14:151:151:61
    3
    19:14:151:151:61
    9
    0
    """
    #94111111111111111111111111111111111111

    """ 4
        1914f1f161
        4
        1914f1f161
        7
        0
    """