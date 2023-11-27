from collections import defaultdict


def read_data():
    with open('puzzle06.in', 'r') as f:
        for line in f:
            *cmd, start, _, end = line.strip().split()
            cmd = ' '.join(cmd)
            yield cmd, tuple(int(n) for n in start.split(',')), tuple(int(n) for n in end.split(','))


def set1(lights_config, r, c):
    lights_config[(r, c)] = 1


def set0(lights_config, r, c):
    lights_config[(r, c)] = 0


def toggle(lights_config, r, c):
    lights_config[(r, c)] = 1 - lights_config[(r, c)]


def inc(lights_config, r, c):
    lights_config[(r, c)] += 1


def inc2(lights_config, r, c):
    lights_config[(r, c)] += 2


def dec(lights_config, r, c):
    lights_config[(r, c)] = max(0, lights_config[(r, c)] - 1)


def lights(cmds, ops):
    lights_config = defaultdict(int)

    for cmd, (r_start, c_start), (r_end, c_end) in cmds:
        for r in range(r_start, r_end + 1):
            for c in range(c_start, c_end + 1):
                ops[cmd](lights_config, r, c)
    return sum(lights_config.values())


def part_1():
    ops = {'turn on': set1, 'turn off': set0, 'toggle': toggle}
    return lights(cmds=read_data(), ops=ops)


def part_2():
    ops = {'turn on': inc, 'turn off': dec, 'toggle': inc2}
    return lights(cmds=read_data(), ops=ops)
