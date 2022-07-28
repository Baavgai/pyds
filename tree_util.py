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
