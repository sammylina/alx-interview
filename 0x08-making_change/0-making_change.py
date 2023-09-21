#!/usr/bin/python3
"""MakeChange module
"""


def makeChange(coins: list, total: int) -> int:
    """ Given a pile of coins , determine the fewest
        number of coins needed to make total
    """
    if len(coins) == 0 or total <= 0:
        return -1
    coins: list = sorted(coins)
    remaining_total: int = total
    coins_count: int = 0
    while remaining_total:
        if len(coins) == 0:
            return -1
        coin: int = coins.pop()
        if remaining_total < coin:
            return -1
        coins_count += remaining_total // coin
        remaining_total = remaining_total % coin
    return coins_count
