#!/usr/bin/python3
"""
Minimum operations.

Try: Copy & Paste
Then: Paste
"""


def minOperations(n: int) -> int:
    """Minimum operations to achieve a number."""
    if (n <= 1):
        return 0

    num = 2
    clip = 1
    ops = 2
    while num <= n:
        # print(f"{num}, {clip}  Ops: {ops}")
        if num == n:
            return ops
        if n % num == 0:
            clip = num
            num *= 2
            ops += 2
        else:
            num += clip
            ops += 1

    return 0
