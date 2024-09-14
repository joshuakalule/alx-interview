#!/usr/bin/python3
"""
Task: Island Perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of the island desribed in grid"""

    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            # print(grid[r][c])
            if grid[r][c] == 0:
                continue
            L = len(grid[r])
            H = len(grid)
            # top
            if r - 1 < 0 or r - 1 >= 0 and grid[r - 1][c] == 0:
                perimeter += 1
            # bottom
            if r + 1 >= H or r + 1 < H and grid[r + 1][c] == 0:
                perimeter += 1
            # right
            if c + 1 >= L or c + 1 < L and grid[r][c + 1] == 0:
                perimeter += 1
            # left
            if c - 1 < 0 or c - 1 >= 0 and grid[r][c - 1] == 0:
                perimeter += 1
    return perimeter
