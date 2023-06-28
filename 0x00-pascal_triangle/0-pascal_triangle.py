#!/usr/bin/env python3
""" pascal_triangle module
"""


def pascal_triangle(n):
    """ Print a pascal triangle with n rows
    """

    main_arr = []
    for row in range(1, n + 1):
        arr = []
        for col in range(1, row + 1):
            if col == 1 or col == row:
                arr.append(1)
            elif col < row:
                val = main_arr[row - 2][col - 1] + main_arr[row - 2][col - 2]
                arr.append(val)
        main_arr.append(arr)
    return main_arr
