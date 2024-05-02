from numpy import array

import matrix.main as mtx
from util.env_vars import config


def matrix_2(timestamp: str) -> None:
    mxA = array([
        [1,  2,  3,  4,  5,  6,  7,  8,  9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18]
    ])

    mxB = array([
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10],
        [11, 12],
        [13, 14],
        [15, 16],
        [17, 18],
    ])

    if config["verbose"]:
        print("Matrix A:")
        print(mxA)
        print("\n")
        print("Matrix B:")
        print(mxB)

    result = []
    result.append(mtx.matrix_multiplication(mxA, mxB))
    result.append(mtx.matrix_multiplication_check(mxA, mxB))

    if config["verbose"]:
        print("\n")
        print(f"Test matrix 2 - {timestamp}")
        print("\n")
        print(f"Result: \n{result[0]}")
        print("\n")
        print(f"Verification: \n{result[1]}")
