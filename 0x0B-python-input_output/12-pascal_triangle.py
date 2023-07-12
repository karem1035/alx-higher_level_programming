#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Function that returns a list of integers
    representing the Pascal's triangle of n"""

    if (n <= 0):
        return ([])

    elif (n == 1):
        return ([[1]])

    elif (n == 2):
        return ([[1], [1, 1]])

    pascal_triangle = [[1], [1, 1]]

    for i in range(1, n - 1):
        new_list = []
        new_list.append(1)
        for j in range(1, len(pascal_triangle)):
            new_list.append(pascal_triangle[i][j - 1] + pascal_triangle[i][j])
        new_list.append(1)
        pascal_triangle.append(new_list)

    return (pascal_triangle)
