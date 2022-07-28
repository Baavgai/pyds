import random

def test_data(size = 10, max_value = 10):
    for _ in range(size):
        yield random.randint(1, max_value + 1)

def test_data_u(max_value = 10):
    return sorted(range(1, max_value + 1), key=lambda x: random.random())

def insert_data(container, data):
    result = container.create()
    for x in data:
        result = container.insert_value(result, x)
    return result

def step_test(container, data = (6,3,9,1,8,4,10)):
    print('step_test', container.__name__)
    x = container.create()
    print('empty',x)
    for (i,n) in enumerate(data):
        x = container.insert_value(x, n)
        print(i, n, x)
    print()