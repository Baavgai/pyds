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

traverse = traverse_ordered

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
    def loop(node, pos):
        if node is not None:
            (value, left, right) = node
            yield from loop(left, pos + '0')
            yield (value, len(pos) - 1, int(pos, 2))
            yield from loop(right, pos + '1')
    h = height(tree)
    cols = 1 << h
    a = [[0 for i in range(cols)] for j in range(h)]
    for (value, row, col) in loop(tree, '0'):
        a[row][col] = value
    for x in a:
        print(x)
