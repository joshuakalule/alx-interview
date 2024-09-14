#!/usr/bin/python3
"""
Task: Island Perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of the island desribed in grid"""

    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            cell = grid[r][c]
            if cell == 0:
                continue
            # top
            if r - 1 >= 0 and grid[r - 1][c] == 0:
                perimeter += 1
            # bottom
            if r + 1 < len(grid) and grid[r + 1][c] == 0:
                perimeter += 1
            # right
            if c + 1 < len(grid[r]) and grid[r][c + 1] == 0:
                perimeter += 1
            # left
            if c - 1 >= 0 and grid[r][c - 1] == 0:
                perimeter += 1
            # last row
            if r + 1 >= len(grid):
                perimeter += 1
            # last column
            if c + 1 >= len(grid[r]):
                perimeter += 1
    return perimeter
