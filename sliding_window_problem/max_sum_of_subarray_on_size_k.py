def solve(arr, k):
    """
    https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

    Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

    Example 1:

    Input:
    N = 4, K = 2
    Arr = [100, 200, 300, 400]
    Output:
    700
    Explanation:
    Arr3  + Arr4 =700,
    which is maximum.
    :param arr:
    :param k:
    :return:
    """
    n = len(arr)
    i = 0
    j = i
    m = float('-inf')
    s = 0
    while j < n:
        s += arr[j]
        if (j - i + 1) < k:
            j += 1
        elif (j - i + 1) == k:
            m = max(s, m)
            j += 1
            s -= arr[i]
            i += 1

    return m
print(solve([100, 200, 300, 400], 2))