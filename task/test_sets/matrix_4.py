from numpy.random import randint

from util.env_vars import config
from matrix.main import matrix_multiplication as mtx
from matrix.main import matrix_multiplication_check as mtxck


def matrix_4(timestamp: str) -> None:
    mxA = randint(config["mtx_min"], config["mtx_max"] + 1, size=(3, 4))
    mxB = randint(config["mtx_min"], config["mtx_max"] + 1, size=(4, 5))
    mxC = randint(config["mtx_min"], config["mtx_max"] + 1, size=(5, 3))

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
        print(f"Test matrix 4 - {timestamp}")
        print("\n")
        print(f"Result: \n{result[0]}")
        print("\n")
        print(f"Verification: \n{result[1]}")
