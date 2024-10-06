#!/usr/bin/python3
"""
0-pascal-triangle
"""


def pascal_triangle(n):
    """
    Get the triangle of n elements
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        line = [1]
        for j in range(1, i):
            line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        line.append(1)
        triangle.append(line)
    return triangle
