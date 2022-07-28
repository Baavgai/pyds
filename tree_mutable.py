from tree_util import *


def create():
    return None


def create_node(value, left=None, right=None):
    return [value, left, right]


def insert_value(tree, value):
    def loop(current_node):
        (tree_value, left, right) = current_node
        if value < tree_value:
            if left is None:
                current_node[1] = create_node(value) 
            else:
                insert_value(left, value)
        else:
            if right is None:
                current_node[2] = create_node(value) 
            else:
                insert_value(right, value)
    if tree is None:
        return create_node(value)
    else:
        loop(tree)
        return tree
