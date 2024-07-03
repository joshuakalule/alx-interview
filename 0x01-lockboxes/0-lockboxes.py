#!/usr/bin/python3
"""
Given n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to
the other boxes.

This is a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Implementation of lockbox algorithm."""
    if not boxes:
        return False

    opened = set()
    stack = [0]

    while stack:
        idx = stack.pop()
        # print(f"in box[{idx}] {boxes[idx]}, opened {opened}, stack {stack}")
        if idx not in opened:
            opened.add(idx)
            for key in boxes[idx]:
                if key not in opened and key not in stack:
                    stack.append(key)

    return (len(opened) == len(boxes))
