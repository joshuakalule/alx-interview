#!/usr/bin/python3
"""Minimum operations."""


def minOperations(n: int) -> int:
    if n <= 1:
        return 0

    # Initialize the current length and operations count
    current_length = 1
    min_operations = 0

    while current_length < n:
        if n % current_length == 0:
            # If current_length divides n, we can use "Copy All" and "Paste"
            current_length *= 2
            min_operations += 1
        else:
            # Otherwise, we can only "Paste" the existing content
            current_length += current_length
            min_operations += 1

    return min_operations
