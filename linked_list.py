# linked list container

def create():
    return None

def create_node(value, next=None):
    return (value, next)

def insert_value(container, value):
    return create_node(value, container)

def traverse(container):
    while container is not None:
        yield container[0]
        container = container[1]
