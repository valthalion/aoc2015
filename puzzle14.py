testing = False


class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self.cycle = duration + rest
        self.position = 0
        self.time = 0
        self.score = 0
        self.running = True
        self.next_change = duration

    def distance(self, time):
        cycles, part = divmod(time, self.cycle)
        flying_time = cycles * self.duration + min(self.duration, part)
        return flying_time * self.speed

    def time_step(self):
        self.time += 1
        if self.running:
            self.position += self.speed
            if self.time == self.next_change:
                self.running = False
                self.next_change += self.rest
        else:
            if self.time == self.next_change:
                self.running = True
                self.next_change += self.duration

    def get_point(self):
        self.score += 1


def read_data():
    filename = 'puzzle14_test.in' if testing else 'puzzle14.in'
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.strip().split()
            name, speed, duration, rest = tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[13])
            yield Reindeer(name, speed, duration, rest)


def part_1():
    time = 1000 if testing else 2503
    return max(reindeer.distance(time) for reindeer in read_data())


def part_2():
    time = 1000 if testing else 2503
    reindeers = tuple(read_data())
    for _ in range(time):
        for reindeer in reindeers:
            reindeer.time_step()
        best = max(reindeer.position for reindeer in reindeers)
        for reindeer in reindeers:
            if reindeer.position == best:
                reindeer.get_point()
    return max(reindeer.score for reindeer in reindeers)
