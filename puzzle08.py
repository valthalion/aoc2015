testing = False


def read_data():
    filename = 'puzzle08_test.in' if testing else 'puzzle08.in'
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


def count_len(line):
    total_len = len(line)
    string_len = 0
    line_iter = iter(line)
    c = next(line_iter)  # consume starting double quote
    if c != '"':
        raise RuntimeError('String does not start with double quote')
    while True:
        c = next(line_iter)
        if c == '"':
            break
        if c == '\\':
            c = next(line_iter)
            if c in '\\"':
                pass
            elif c == 'x':
                _, _ = next(line_iter), next(line_iter)
            else:
                raise RuntimeError('Unknown escape sequence:', c)
        string_len += 1
    return total_len, string_len


def count_len2(line):
    total_len = len(line)
    string_len = sum(2 if c in '\\"' else 1 for c in line) + 2  # add the new quotes on either end
    return total_len, string_len


def part_1():
    delta = 0
    for line in read_data():
        total_len, string_len = count_len(line)
        delta += total_len - string_len
    return delta


def part_2():
    delta = 0
    for line in read_data():
        total_len, string_len = count_len2(line)
        delta += string_len - total_len
    return delta
