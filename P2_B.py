
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
