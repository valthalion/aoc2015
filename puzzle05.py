import re


repeat_re = re.compile(r'(.{2}).*\1')
between_re = re.compile(r'(.).\1')


def read_data():
    with open('puzzle05.in', 'r') as f:
        for line in f:
            yield line.strip()


vowels = set('aeiou')
naughty_strings = tuple(tuple(s) for s in ('ab', 'cd', 'pq', 'xy'))


def three_plus_vowels(s):
    return sum(1 for c in s if c in vowels) >= 3


def double(s):
    return any(s[idx] == s[idx+1] for idx in range(len(s) - 1))


def not_naughty(s):
    for pair in zip(s, s[1:]):
        if pair in naughty_strings:
            return False
    return True


def is_nice(s):
    return all(pred(s) for pred in (three_plus_vowels, double, not_naughty))


def is_nice2(s):
    return repeat_re.search(s) and between_re.search(s)


def part_1():
    return sum(1 for s in read_data() if is_nice(s))


def part_2():
    return sum(1 for s in read_data() if is_nice2(s))
