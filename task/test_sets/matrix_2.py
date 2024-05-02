from numpy import array

import matrix.main as mtx
from util.env_vars import config
from util.files import save_as_csv


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
        print(f"MTX_2-{timestamp}")
        print("\n")
        print(f"Result: \n{result[0]}")
        print("\n")
        print(f"Verification: \n{result[1]}")

    save_as_csv(mxA, f"MTX_2-mxA-{timestamp}")
    save_as_csv(mxB, f"MTX_2-mxB-{timestamp}")
    save_as_csv(result[0], f"MTX_2-result-{timestamp}")
    save_as_csv(result[1], f"MTX_2-result-{timestamp}")
