#!/usr/bin/env python3
"""Rorate 2D matrix module
"""


def rotate_2d_matrix(matrix):
    """ Transpose a  matrix
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r == c:
                pass
            elif matrix[r][c] is not None and matrix[c][r] is not None:
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    return matrix
