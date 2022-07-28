from shared import test_data_u, insert_data

def traverse_preorder(container):
    if container is not None:
        (value, left, right) = container
        yield value
        yield from traverse_preorder(left)
        yield from traverse_preorder(right)


def traverse_postorder(container):
    if container is not None:
        (value, left, right) = container
        yield from traverse_postorder(left)
        yield from traverse_postorder(right)
        yield value


def traverse_ordered(container):
    if container is not None:
        (value, left, right) = container
        yield from traverse_ordered(left)
        yield value
        yield from traverse_ordered(right)


def tree_test_data(container, data):
    raw = [x for x in data]
    print('tree test', container.__name__)
    print('raw data', raw)
    xs = insert_data(container, raw)
    print('raw container', xs)
    for f in (traverse_preorder, traverse_postorder, traverse_ordered):
        print(f.__name__, [x for x in f(xs)])
    print()

def tree_test(container, n = 10):
    tree_test_data(container, test_data_u(n))
