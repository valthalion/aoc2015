testing = False


op_dict = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'RSHIFT': lambda x, y: x >> y,
    'LSHIFT': lambda x, y: x << y,
    'NOT': lambda x: ~x,
    'identity': lambda x: x,
}


def operand(value):
    if value.isdecimal():
        return int(value)
    return value


def read_data():
    nodes = {}
    filename = 'puzzle07_test.in' if testing else 'puzzle07.in'
    with open(filename, 'r') as f:
        for line in f:
            operation, node_name = line.strip().split(' -> ')
            tokens = operation.split()
            if len(tokens) == 1:  # leaf or direct connection
                child = operand(tokens[0])
                if isinstance(child, int):  # leaf
                    nodes[node_name] = Node(node_name, op=None, children=child)
                else:
                    nodes[node_name] = Node(node_name, op=op_dict['identity'], children=(child,))
            elif len(tokens) == 2:  # unary
                nodes[node_name] = Node(node_name, op=op_dict[tokens[0]], children=(operand(tokens[1]),))
            else:  # binary
                children = (operand(tokens[0]), operand(tokens[2]))
                nodes[node_name] = Node(node_name, op=op_dict[tokens[1]], children=children)
    for node in nodes.values():
        if isinstance(node.children, int):
            continue
        node.children = tuple(child if isinstance(child, int) else nodes[child] for child in node.children)
    return nodes


class Node:
    def __init__(self, name, op, children):
        self._value = None
        self.name = name
        self.op = op
        self.children = children
        if self.op is None:
            self._value = children

    @property
    def value(self):
        if self._value is None:
            self._value = self.op(*(child if isinstance(child, int) else child.value for child in self.children))
        return self._value


def adjust(value):
    if value < 0:
        return 65536 + value
    return value


def part_1():
    nodes = read_data()
    if testing:
        for node in nodes.values():
            print(node.name, adjust(node.value))
        return
    return nodes['a'].value


def part_2():
    nodes = read_data()
    nodes['b']._value = 3176
    return nodes['a'].value
