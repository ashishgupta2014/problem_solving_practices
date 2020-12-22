"""
https://app.glider.ai/practice/problem/algorithms/number-of-all-subsequences-having-product-less-tha/problem

https://www.geeksforgeeks.org/count-subsequences-product-less-k/

For a given array find the number of subsequences having product smaller than integer K.

Input
The first line of input contains an integer N, representing the size of the array.
The second line of input contains N space-separated integers, representing the array elements.
The third line of input contains an integer K, as described in the problem statement.

Output
A number of subsequences having product smaller than K.

Constraints
1 <= N <=106
1 <= K <=106

"""





import numpy as np
def product(arr, K):
    """
    non optimized
    :param arr:
    :param K:
    :return:
    """
    lists = [[]]
    count = 0
    for i in range(len(arr)):
        orig = lists[:]
        new = arr[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
            result1 = np.prod(lists[j])
            if result1 < K:
                count += 1
        lists = orig + lists
    print(lists)
    print(count)
arr = list(map(int, '1 2 3 4'.split()))
product(arr, 10)


def productSubSeqCount(arr, k):
    """
    Optimized version of code
    :param arr:
    :param k:
    :return:
    """
    n = len(arr)
    dp = [[0 for i in range(n + 1)]
          for j in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):

            # number of subsequence
            # using j-1 terms
            dp[i][j] = dp[i][j - 1]

            # if arr[j-1] > i it will
            # surely make product greater
            # thus it won't contribute then
            if arr[j - 1] <= i and arr[j - 1] > 0:
                # number of subsequence
                # using 1 to j-1 terms
                # and j-th term
                dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
    return dp[k][n]
A = [1,2,3,4]
k = 10
print(productSubSeqCount(A, k))