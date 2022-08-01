def height(tree):
    if tree is None:
        return 0
    (_, left, right) = tree
    return 1 + max(height(left), height(right))


# function to check if tree is height-balanced or not
def is_balanced(tree):
    if tree is None:
        return True
    (_, left, right) = tree
    return (abs(height(left) - height(right)) <= 1) and is_balanced(left) and is_balanced(right)


def traverse_preorder(tree):
    if tree is not None:
        (value, left, right) = tree
        yield value
        yield from traverse_preorder(left)
        yield from traverse_preorder(right)


def traverse_postorder(tree):
    if tree is not None:
        (value, left, right) = tree
        yield from traverse_postorder(left)
        yield from traverse_postorder(right)
        yield value


def traverse_ordered(tree):
    if tree is not None:
        (value, left, right) = tree
        yield from traverse_ordered(left)
        yield value
        yield from traverse_ordered(right)


def traverse_ordered_flat(tree):
    nodes = [tree]
    while nodes != []:
        node = nodes.pop()
        if node is not None:
            (value, left, right) = node
            if left is None and right is None:
                yield value
            else:
                nodes.append(right)
                nodes.append((value, None, None))
                nodes.append(left)


traverse = traverse_ordered

def tree_to_list(tree):
    if tree is not None:
        nodes = [(tree, '0')]
        while nodes != []:
            node = nodes.pop()
            if node is not None:
                ((value, left, right), pos) = node
                yield ((len(pos) - 1, int(pos, 2)), value)
                if right is not None:
                    nodes.append((right, pos + '1'))
                if left is not None:
                    nodes.append((left, pos + '0'))

def tree_info_dump(tree):
    def loop(node, pos):
        if node is not None:
            (value, left, right) = node
            yield from loop(left, pos + '0')
            yield (value, len(pos), int(pos, 2))
            yield from loop(right, pos + '1')
    for x in sorted(loop(tree, '0'), key=lambda x: x[1]):
        print(x)
    h = height(tree)
    print('height', h)
    print('foot size', 1 << h)


def tree_to_text(tree):
    h = height(tree)
    d = dict(tree_to_list(tree))
    w = 1 << h
    w *= 2
    cols = 1
    for row in range(h):
        line = f"{row} "
        for col in range(cols):
            k = (row, col)
            if k in d:
                line += f"{d[k]}".center(w)
            else:
                line += "---".center(w)
        print(line)
        cols = cols << 1
        w = w // 2

