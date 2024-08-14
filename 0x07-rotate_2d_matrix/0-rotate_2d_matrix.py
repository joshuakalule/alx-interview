#!/usr/bin/python3
"""Task 0. Rotate 2D matrix"""


def rotate_2d_matrix(matrix: list) -> None:
    """Implement inplace 2D matrix rotation of 90°."""
    # 1. transpose matrix
    for i, new_row in enumerate(zip(*matrix)):
        matrix[i] = new_row
    # 2. reverse rows
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
