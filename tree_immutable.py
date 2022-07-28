# from tree_util import height, is_balanced, traverse_ordered as traverse
from tree_util import *

def create():
    return None


def create_node(value, left=None, right=None):
    return (value, left, right)


def insert_value(tree, value):
    def loop(tree_value, left, right):
        if value < tree_value:
            if left is None:
                return create_node(tree_value, create_node(value), right)
            else:
                return create_node(tree_value, insert_value(left, value), right)
        else:
            if right is None:
                return create_node(tree_value, left, create_node(value))
            else:
                return create_node(tree_value, left, insert_value(right, value))
    if tree is None:
        return create_node(value)
    else:
        return loop(*tree)



