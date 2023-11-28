from collections import defaultdict


testing = False


def read_data():
    filename = 'puzzle09_test.in' if testing else 'puzzle09.in'
    graph = defaultdict(dict)
    with open(filename, 'r') as f:
        for line in f:
            nodes, dist = line.strip().split(' = ')
            dist = int(dist)
            orig, dest = nodes.split(' to ')
            graph[orig][dest] = dist
            graph[dest][orig] = dist
    return graph


def tsp(graph, reduction=min, close_tour=False):
    def _tsp(path, path_len):
        if len(path) == len(graph):
            if close_tour:
                path_len += graph[path[-1]][path[0]]
            return path_len, path
        return reduction(_tsp((*path, node), path_len + graph[path[-1]][node]) for node in set(graph) - set(path))

    return reduction(_tsp(path=(node,), path_len=0) for node in graph)


def part_1():
    path_len, path = tsp(graph=read_data())
    print(path)
    return path_len


def part_2():
    path_len, path = tsp(graph=read_data(), reduction=max)
    print(path)
    return path_len
