# Now provide a function that given 3 arguments representing angles on $x$, $y$ and $z$ respectively returns a combinaed transformation. Try it with different vectors and confirm your results
def task_5(timestamp: str) -> None:
    mxA, mxB = mtx.load_matrix([(2, 3), (3, 2)])

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
        print(f"MTX_1-{timestamp}")
        print("\n")
        print(f"Result: \n{result[0]}")
        print("\n")
        print(f"Verification: \n{result[1]}")

    save_as_csv(mxA, f"MTX_1-mxA-{timestamp}")
    save_as_csv(mxB, f"MTX_1-mxB-{timestamp}")
    save_as_csv(result[0], f"MTX_1-result-{timestamp}")
    save_as_csv(result[1], f"MTX_1-result-{timestamp}")
