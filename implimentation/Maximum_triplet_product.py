import numpy as np

def triplet(arr):
    """
    https://app.glider.ai/tutorials/maximum-triplet-product/problem

    The hiring team of Google aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 3 candidates are great collectively if the product of their abilities is maximum.
    Given the abilities of N candidates, find the maximum collective ability from the given pool of candidates.

    Input
    The first line of input contains an integer N, representing the size of the array.
    The second line of input contains N space-separated integers, representing the array elements.

    Output
    Print the maximum collective ability of three candidates.

    Constraints
    3 ≤ N ≤ 107
    -105 ≤ ability ≤ 105

    :param arr:
    :return:
    """
    arr.sort()
    print(arr)
    print(arr[-3:])
    return max(np.prod(arr[-3:]), np.prod(arr[:2])*arr[-1])


print(triplet(list(map(int, '5 10 3 5 6 20'.split()))))