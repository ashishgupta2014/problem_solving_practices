"""
https://app.glider.ai/tutorials/adjacent-houses-maximum-sum-nonadjacent/problem

https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

Given an array ar[] of positive integers. Find the maximum sum of a sub set such that no two numbers in the sequence
should be adjacent in the array.

Input
The first line of input contains an integer N, denotes the size of array ar[].
The second line of input contains N space-separated integers, denoting the array elements.

Output
Print the maximum sum of a sub set.

Constraints
1 ≤ N ≤ 106
1 ≤ ar[i] ≤ 107

Example #1
Input
6
5 5 10 100 10 5
Output
110
Explanation: 5 + 100 + 5(5 at index 1, 100 at index 3 and 5 and index 5).

Example #2
Input
4
3 2 7 10
Output
13
Explanation: 3 and 10 forms a non-continuous sub set with maximum sum.
"""

def maxSum(ar):
    """

    :param ar:
    :return:
    """
    s = 0
    n = len(ar)
    i = 0
    l = float('-inf')

    while i < n:
        if (i == 0 and ar[i] >= ar[i+1]) or (i == n - 1 and i-1 != l):
            s += ar[i]
            l = i
        else:
            if ar[i-1] <= ar[i] and ar[i] >= ar[i+1] and i-1 != l:
                s += ar[i]
                l = i
        print(i, '==>', s)
        i += 1
    return s


ar = [10, 5, 10, 10, 100, 5]

print(maxSum(ar))


def maximum_sum(ar):
    """

    :param ar:
    :return:
    """
    n = len(ar)
    if n == 0:
        return 0
    elif n == 1:
        return ar[0]
    elif n == 2:
        return max(ar[0], ar[1])
    else:
        dp = [0] * n
        dp[0] = ar[0]
        dp[1] = max(ar[0], ar[1])
        for i in range(1, len(ar)):
            dp[i] = max(ar[i] + dp[i-2], dp[i-1])
        return dp[-1]
ar = [10, 5, 10, 10, 100, 5]

print(maximum_sum(ar))