import json


def read_data():
    with open('puzzle12.in', 'r') as f:
        data = json.load(f)
    return data


def flatten(data, filter_red=False):
    if isinstance(data, int):
        yield data
    elif isinstance(data, list):
        yield from (value for item in data for value in flatten(item, filter_red))
    elif isinstance(data, dict):
        if filter_red and 'red' in data.values():
            return
        yield from (value for item in data.values() for value in flatten(item, filter_red))
    else:  # string value
        return


def part_1():
    data = read_data()
    return sum(flatten(data))


def part_2():
    data = read_data()
    return sum(flatten(data, filter_red=True))
