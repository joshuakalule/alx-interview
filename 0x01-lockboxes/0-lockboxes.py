#!/usr/bin/python3
"""
Given n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to
the other boxes.

This is a method that determines if all the boxes can be opened.
"""


def open(key, opened, map):
    """Helper function to do recursion."""
    opened.add(key)
    print(f"in map[{key}] {map[key]} -- opened {opened}")
    for key in map[key]:
        if key not in map:
            continue
        if key not in opened:
            open(key, opened, map)


def canUnlockAll(boxes):
    """Implementation of lockboxes."""
    opened = set()
    map = {idx: array for idx, array in enumerate(boxes)}
    open(0, opened, map)
    return len(opened) == len(boxes)
