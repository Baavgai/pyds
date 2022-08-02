from graphviz import Digraph

def tree_to_dot(tree):
    def loop(node, name, dot = Digraph(), parent = None):
        if node is None:
            return dot
        (value, left, right) = node
        dot.node(name=name, label=str(value))
        if parent is not None:
            dot.edge(parent, name)
        
        loop(left, name + 'L', dot, name)
        loop(right, name + 'R', dot, name)
        return dot
    return loop(tree, 'X')


if __name__ == "__main__":
    # import tree_util as util
    import tree_immutable as provider
    from shared import insert_data
    from tests import test_data_u

    dot = tree_to_dot(insert_data(provider, test_data_u(40)))
    dot.format = 'png'
    dot.view(filename='digraph', directory='./hold')
