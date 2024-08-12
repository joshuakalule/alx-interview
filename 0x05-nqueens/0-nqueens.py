#!/usr/bin/python3
"""Task 0. N Queens"""

import sys


def n_queens(n: int) -> None:
    """Solve the N QUeens problem for n queens on nxn board"""

    columns = set()
    neg_diag = set()  # (r - c) is the same
    pos_diag = set()  # (r + c) is the same

    placed: list = []

    def backtrack(row: int) -> None:
        """Helper method to backtrack."""
        if row == n:
            print(placed)
            return

        for col in range(n):
            if col in columns:
                continue
            if row - col in neg_diag:
                continue
            if row + col in pos_diag:
                continue

            columns.add(col)
            neg_diag.add(row - col)
            pos_diag.add(row + col)
            placed.append([row, col])

            backtrack(row + 1)

            columns.remove(col)
            neg_diag.remove(row - col)
            pos_diag.remove(row + col)
            placed.remove([row, col])

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isnumeric():
        print("N must be a number")
        exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    n_queens(N)
