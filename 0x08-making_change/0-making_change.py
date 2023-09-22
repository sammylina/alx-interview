#!/usr/bin/python3
"""MakeChange module
"""


def makeChange(coins, total):
    """ Given a pile of coins , determine the fewest
        number of coins needed to make total
    """
    if total <= 0:
        return 0
    coins = sorted(coins)
    remaining_total = total
    coins_count = 0
    while remaining_total:
        if len(coins) <= 0:
            return -1
        coin = coins.pop()
        coins_count += remaining_total // coin
        remaining_total = remaining_total % coin
    return coins_count
