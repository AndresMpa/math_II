from numpy import dot, zeros, ndarray


def matrix_verification(
    matrix_A: ndarray,
    matrix_B: ndarray
) -> None:
    """
    Execute a simple verification to check if 2 matrices are compatible

    Args:
        matrix_A (array): Matrix
        matrix_B (array): Matrix

    Note:
        Raise an error to stop execution
    """
    if matrix_A.shape[1] != matrix_B.shape[0]:
        raise ValueError("Matrices are not compatible. Check their dimension")


def matrix_multiplication_check(
    matrix_A: ndarray,
    matrix_B: ndarray
) -> ndarray:
    """
    Test a multiplication between 2 matrices using numpy options

    Args:
        matrix_A (array): A simple matrix
        matrix_B (array): B simple matrix

    Returns:
        It returns the multiplication of those matrices
    """
    dot_test = dot(matrix_A, matrix_B)
    return dot_test


def matrix_multiplication(
    matrix_A: ndarray,
    matrix_B: ndarray
) -> ndarray:
    """
    Multiply 2 matrices without numpy options

    Args:
        matrix_A (array): A matrix as a numpy array
        matrix_B (array): A matrix as a numpy array

    Returns:
        It returns the multiplication of those matrices
    """
    matrix_verification(matrix_A, matrix_B)

    result_matrix = zeros((matrix_A.shape[0], matrix_B.shape[1]))

    for i in range(matrix_A.shape[0]):
        for j in range(matrix_B.shape[1]):
            for k in range(matrix_A.shape[1]):
                result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result_matrix
