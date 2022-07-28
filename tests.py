import random
from shared import insert_data


def test_data(size = 10, max_value = 10):
    for _ in range(size):
        yield random.randint(1, max_value + 1)


def test_data_u(max_value = 10):
    return sorted(range(1, max_value + 1), key=lambda x: random.random())


def step_test(provider, data = (6,3,9,1,8,4,10)):
    print('step_test', provider.__name__)
    x = provider.create()
    print('empty',x)
    for (i,n) in enumerate(data):
        x = provider.insert_value(x, n)
        print(i, n, x)
    print()


def tree_test_data(provider, data):
    raw = [x for x in data]
    tree = insert_data(provider, raw)
    print('tree test', provider.__name__)
    print('raw data', raw)
    print('raw tree', tree)
    print('height', provider.height(tree))
    print('balanced', provider.is_balanced(tree))
    for f in (provider.traverse_preorder, provider.traverse_postorder, provider.traverse_ordered):
        print(f.__name__, [x for x in f(tree)])
    print()


def tree_test(tree, n = 10):
    tree_test_data(tree, test_data_u(n))

