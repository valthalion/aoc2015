from collections import defaultdict

from puzzle09 import tsp


testing = False


def read_data():
    filename = 'puzzle13_test.in' if testing else 'puzzle13.in'
    graph = defaultdict(dict)
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.strip().split()
            orig, sign, value, dest = tokens[0], (1 if tokens[2] == 'gain' else -1), int(tokens[3]), tokens[-1][:-1]
            value *= sign
            if dest in graph[orig]:
                graph[orig][dest] += value
            else:
                graph[orig][dest] = value
            if orig in graph[dest]:
                graph[dest][orig] += value
            else:
                graph[dest][orig] = value
    return graph


def part_1():
    path_len, path = tsp(graph=read_data(), reduction=max, close_tour=True)
    print(path)
    return path_len


def part_2():
    path_len, path = tsp(graph=read_data(), reduction=max, close_tour=False)
    print(path)
    return path_len
