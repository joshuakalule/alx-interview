#!/usr/bin/python3
"""
Task 0. Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins)

    stack = sorted_coins.copy()

    current_total = int(total)
    count = 0
    while stack:
        coin = stack.pop()
        div = int(current_total / coin)
        rem = current_total % coin
        if div == 0:
            continue
        if rem == 0:
            return count + div
        count += div
        current_total = current_total - (coin * div)
    return -1
