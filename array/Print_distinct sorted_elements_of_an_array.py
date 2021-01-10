def distinctDigits(arr):
    """
    https://app.glider.ai/practice/problem/algorithms/reverse-an-array-or-list/problem

    Given an array of positive integers of size N, The task is to make a sorted array that will contain all
    distinct digits present in the array.

    Input
    The first line of input contains an integer N, representing the size of the array ar[].
    The second line of input contains N space-separated integers, representing the array elements.

    Output
    Print the required array.

    Constraints
    1 <= N <= 107
    1 <= ar[] <= 1016

    Example #1
    Input
    3
    131 11 48
    Output
    1 3 4 8
    Explanation: 1, 3, 4, and 8 are only distinct digits that can be extracted from the values in the array.

    :param arr:
    :return:
    """
    out = set()
    for i in arr:
        for j in str(i):
            out.add(int(j))
    out = list(out)
    out.sort()
    return out
print(distinctDigits([131, 11, 48]))