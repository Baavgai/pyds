from tests import *
import linked_list
import tree_immutable
import tree_mutable

def run_all_tests():
    for m in (linked_list, tree_immutable, tree_mutable):
        step_test(m)
        if m.__name__ != 'linked_list':
            tree_test(m)

run_all_tests()
# print(dir(tree_immutable))
