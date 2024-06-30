#!/usr/bin/python3
"""Pascal's triangle Implementation."""


def value(idx, array):
    """Helper function."""
    if idx < 0 or idx >= len(array):
        return 0
    else:
        return array[idx]


def pascal_triangle(n):
    """Main function to execute pascal's triangle."""
    map = []
    if (n <= 0):
        return map

    map.append([1])
    if (n == 1):
        return map

    for i in range(1, n):
        row = []
        prev_row = map[i - 1]
        prev_row_len = len(prev_row)
        for x in range(prev_row_len + 1):
            num = value(x - 1, prev_row) + value(x, prev_row)
            row.append(num)
        map.append(row)

    return map
