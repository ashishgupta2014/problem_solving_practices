def golomb_sequence(n, arr):
    """
    https://www.geeksforgeeks.org/golomb-sequence/

    In mathematics, the Golomb sequence is a non-decreasing integer sequence where n-th term is equal to number of
    times n appears in the sequence.

    The first few values are
    1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, ……

    Explanation of few terms:
    Third term is 2, note that three appears 2 times.
    Second term is 2, note that two appears 2 times.
    Fourth term is 3, note that four appears 3 times.

    Given a positive integer n. The task is to find the first n terms of Golomb sequence.

    :param n:
    :return:
    """
    if n == 1:
        return 1
    if arr[n] != 0:
        return arr[n]
    arr[n] = 1 + golomb_sequence(n - golomb_sequence(golomb_sequence(n - 1, arr), arr), arr)
    return arr[n]
n = 6
arr = [0] * (n+1)
for i in range(1, n + 1):
        print(golomb_sequence(i, arr), end=" ")
