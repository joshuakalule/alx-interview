#!/usr/bin/python3
"""Minimum operations."""

from typing import Tuple


def recurse(num_clip: Tuple[int, int], ops: int, n: int) -> int:
    """Handle recursion."""
    num, clip = num_clip
    if num == n:
        return ops
    if num <= 0 | num > n | clip >= n:
        return ops
    res_paste = recurse((num + clip, clip), ops+1, n)
    res_copy_n_paste = recurse((num + num, num), ops+2, n)

    print(f"P: {res_paste}, CP: {res_copy_n_paste}")

    if res_paste > n and res_copy_n_paste > n:
        return 0
    if min(res_paste, res_copy_n_paste) == 0:
        return max(res_paste, res_copy_n_paste)
    return min(res_paste, res_copy_n_paste)


def minOperations(n):
    """Minimum operations to achieve a number."""
    return recurse((2, 1), 2, n)


if __name__ == '__main__':

    print(minOperations(12))
