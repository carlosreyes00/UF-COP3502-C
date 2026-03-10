def convert(data):
    new_data = {}

    for item in data:
        category = item["type"]
        name = item["name"]
        price = item["price"]

        if category not in new_data:
            new_data[category] = {}

        new_data[category][name] = price

    return new_data