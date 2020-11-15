def solve(arr, k):
    """
    https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
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