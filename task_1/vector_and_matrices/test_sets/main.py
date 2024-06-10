from test_sets.vector_1 import vector_1
from test_sets.vector_2 import vector_2
from test_sets.vector_3 import vector_3
from test_sets.vector_4 import vector_4
from test_sets.matrix_1 import matrix_1
from test_sets.matrix_2 import matrix_2
from test_sets.matrix_3 import matrix_3
from test_sets.matrix_4 import matrix_4

test = {
    "1": vector_1,
    "2": vector_2,
    "3": vector_3,
    "4": vector_4,
    "5": matrix_1,
    "6": matrix_2,
    "7": matrix_3,
    "8": matrix_4
}


def select_stage(mode):
    return test.get(mode, "Error")
