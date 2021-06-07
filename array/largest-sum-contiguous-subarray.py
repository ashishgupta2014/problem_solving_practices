"""
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Largest Sum Contiguous Subarray
Difficulty Level : Medium
Last Updated : 15 Apr, 2021
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers that has the largest sum.
"""
def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


# Driver function to check the above function
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))