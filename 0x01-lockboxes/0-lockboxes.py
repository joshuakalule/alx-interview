#!/usr/bin/python3
"""
Given n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to
the other boxes.

This is a method that determines if all the boxes can be opened.
"""


def open(key, opened, map):
    """Helper function to do recursion."""
    # print(f"in map[{key}] {map[key]} -- opened {opened}")
    opened.append(key)
    for key in map[key]:
        if key not in map:
            continue
        if key not in opened:
            return open(key, opened, map)
    return set(opened)


def canUnlockAll(boxes):
    """Implementation of lockboxes."""
    opened = [0]
    map = {idx: array for idx, array in enumerate(boxes)}

    open(0, opened, map)

    return len(opened) == len(boxes)
