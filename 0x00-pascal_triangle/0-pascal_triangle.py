#!/usr/bin/python3
"""
0-pascal-triangle
"""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def combination(n, r):
    return (factorial(n)) / (factorial(r) * factorial(n - r))


def pascal_triangle(n):
    # Pascal triangle of n
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        line = []
        for j in range(0, i + 1):
            line.append(int(combination(i, j)))
        triangle.append(line)
    return triangle
