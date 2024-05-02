from numpy import array

from util.env_vars import config
from util.files import save_as_csv
from matrix.main import matrix_multiplication as mtx
from matrix.main import matrix_multiplication_check as mtxck


def matrix_3(timestamp: str) -> None:
    mxA = array([
        [1, 2],
        [3, 4]
    ])
    mxB = array([
        [5, 6],
        [7, 8]
    ])
    mxC = array([
        [9, 10],
        [11, 12]
    ])

    if config["verbose"]:
        print("Matrix A:")
        print(mxA)
        print("\n")
        print("Matrix B:")
        print(mxB)
        print("Matrix C:")
        print(mxC)

    result = []
    result.append(mtx(mxA, mtx(mxB, mxC)))
    result.append(mtxck(mxA, mtxck(mxB, mxC)))

    if config["verbose"]:
        print("\n")
        print(f"MTX_3-{timestamp}")
        print("\n")
        print(f"Result: \n{result[0]}")
        print("\n")
        print(f"Verification: \n{result[1]}")

    save_as_csv(mxA, f"MTX_3-mxA-{timestamp}")
    save_as_csv(mxB, f"MTX_3-mxB-{timestamp}")
    save_as_csv(result[0], f"MTX_3-result-{timestamp}")
    save_as_csv(result[1], f"MTX_3-result-{timestamp}")
