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

    stack = [(2, 1, 2)]

    while len(stack) > 0:
        num, clip, ops = stack.pop()
        # print(f"{num}, {clip}  Ops: {ops}")
        if num == n:
            return ops
        # paste only
        if num + clip <= n:
            stack.append((num+clip, clip, ops+1))
        # copy and paste
        if num * 2 <= n:
            stack.append((num*2, num, ops+2))

    return 0
