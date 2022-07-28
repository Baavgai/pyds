from shared import *
from shared_tree import tree_test
import linked_list
import tree_immutable
import tree_mutable

for m in (linked_list, tree_immutable, tree_mutable):
    step_test(m)
    if m.__name__ != 'linked_list':
        tree_test(m)
