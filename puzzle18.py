testing = False
size = 6 if testing else 100
corners = {(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)}


def read_data(stuck_corners=False):
    filename = 'puzzle18_test.in' if testing else 'puzzle18.in'
    with open(filename, 'r') as f:
        lights = {
            (r, c)
            for r, line in enumerate(f)
            for c, value in enumerate(line.strip())
            if value == '#'
        }
    if stuck_corners:
        lights |= corners
    return lights


def neighbours(r, c):
    return {
        (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
        (r , c - 1), (r , c + 1),
        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
    }


def step(lights, stuck_corners=False):
    new_lights = {
        (r, c)
        for r in range(size)
        for c in range(size)
        if (
            ((r, c) in lights and 2 <= len(neighbours(r, c) & lights) <= 3) or
            ((r, c) not in lights and len(neighbours(r, c) & lights) == 3)
        )
    }
    if stuck_corners:
        new_lights |= corners
    return new_lights


def part_1():
    lights = read_data()
    for _ in range(4 if testing else 100):
        lights = step(lights)
    return len(lights)


def part_2():
    lights = read_data(stuck_corners=True)
    for _ in range(5 if testing else 100):
        lights = step(lights, stuck_corners=True)
    return len(lights)
