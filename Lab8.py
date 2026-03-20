def print_backwards(string_to_print):
    if len(string_to_print) == 1:
        print(string_to_print[0], end="")
    else:
        print(string_to_print[len(string_to_print) - 1], end="")
        print_backwards(string_to_print[0:len(string_to_print)-1])

def sum_a(data):
    total = 0
    for item in data:
        total += item.get("a",0)

    return total

def process_list(data):

    even = []
    odd = []

    for i, item in enumerate(data):
        if i % 2 == 0:
            even.append(str(item))
        else:
            odd.append(item*10)

    return even + odd

def group_by(values, func):
    if len(values) == 0:
        return {}

    rest = group_by(values[1:], func)
    key = func(values[0])

    if key in rest:
        rest[key] = [values[0]] + rest[key]
        group = rest.pop(key)
        return {key: group, **rest}
    else:
        return {key: [values[0]], **rest}

def format_names(names):
    if names == []:
        return []

    name = names[0]

    if "," in name:
        formatted = name
    else:
        first, last = name.split(" ")
        formatted = f"{last}, {first}"

    return [formatted] + format_names(names[1:])