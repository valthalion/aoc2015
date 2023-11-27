def read_data():
    with open('puzzle02.in', 'r') as f:
        for line in f:
            yield tuple(sorted(int(n) for n in line.strip().split('x')))


def paper(s1, s2, s3):
    return 3*s1*s2 + 2*s1*s3 + 2*s2*s3


def ribbon(s1, s2, s3):
    return 2 * (s1 + s2) + s1*s2*s3


def part_1():
    return sum(paper(*package) for package in read_data())


def part_2():
    return sum(ribbon(*package) for package in read_data())
