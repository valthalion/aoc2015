from hashlib import md5


key = b'yzbqklnj'


def find_hash(prefix, first_try=1):
    n = first_try
    while True:
        h = md5(b''.join((key, str(n).encode()))).hexdigest()
        if h.startswith(prefix):
            return n
        n += 1


def part_1():
    return find_hash(prefix='00000')


def part_2():
    return find_hash(prefix='000000', first_try=282749)
