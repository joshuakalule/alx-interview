#!/usr/bin/python3
"""Pascal's triangle Implementation."""

def pascal_triangle(n):
    """Main function to execute pascal's triangle."""
    map = []
    if (n <= 0):
        return map

    map.append([1])

    for i in range(2, n, 1):
        print(i)
