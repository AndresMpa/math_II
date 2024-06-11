from util.env_vars import config
from util.files import save_as_csv
from matrix.main import load_matrix
from matrix.main import matrix_multiplication as mtx
from matrix.main import matrix_multiplication_check as mtxck


def matrix_3(timestamp: str) -> None:
    mxA, mxB, mxC = load_matrix([(2, 2), (2, 2), (2, 2)])

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