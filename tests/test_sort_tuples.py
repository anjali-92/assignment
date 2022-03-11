from copy import deepcopy
from src import tuple_sort as ts
from tests import testdata as td

def test_sort_tuples_with_priority():
    # sort updates input tuples list.
    ts.sort_tuples_with_priority(td.tups)
    assert td.exp_out_tups == td.tups