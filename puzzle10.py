def count_encoding(seq):
    last, count = None, 0
    for current in seq:
        if current == last:
            count += 1
            continue
        if last is not None:
            yield count
            yield last
        last, count = current, 1
    yield count
    yield last


def part_1():
    seq = tuple(int(n) for n in '1321131112')
    for _ in range(40):
        seq = tuple(count_encoding(seq))
    return len(seq)


def part_2():
    seq = tuple(int(n) for n in '1321131112')
    for _ in range(50):
        seq = tuple(count_encoding(seq))
    return len(seq)
