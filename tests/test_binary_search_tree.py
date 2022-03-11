from src import binary_search_tree as bst
from tests import testdata as td

def test_bst_insert():
    root = None
    
    for element in td.insert_elements:
        root = bst.insert_into_bst(root, element)
    
    output = []
    expected_output = [1, 10, 12, 13, 14, 24]
    bst.print_bst_inorder(root, output)
    assert expected_output == output


def test_bst_delete():
    root = None
    for element in td.insert_elements:
        root = bst.insert_into_bst(root, element)

    # tests delete output
    after_delete_exp_output = [10, 12, 13, 24]
    for element in td.delete_elements:
        root = bst.delete_from_bst(root, element)
    after_delete_output = []
    bst.print_bst_inorder(root, after_delete_output)
    assert after_delete_exp_output == after_delete_output
