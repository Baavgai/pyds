import tree_immutable as provider
from tree_util import tree_to_text, tree_to_list
from shared import insert_data
from tests import test_data_u

data = test_data_u(10)
tree = insert_data(provider, data)
print('data', data)
print('tree', tree)
tree_to_text(tree)
# print(int('101',2))
# print([x for x in tree_to_list(tree)])