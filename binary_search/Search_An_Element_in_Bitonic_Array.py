def max_ele_index(nums):
    """
    https://leetcode.com/problems/find-peak-element/
    A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.


FIND MAXIMUM ELEMENT IN AN BITONIC ARRAY:

    :param nums:

    :return:
    """
    n = len(nums)
    nums = [float('-inf')] + nums + [float('-inf')]
    if (n == 1): return 0
    l = 1
    r = n
    while l <= n:
        mid = l + (r - l) // 2
        curr = nums[mid]
        left = nums[mid - 1]
        right = nums[mid + 1]
        if (curr > left and curr > right):
            return mid - 1
        elif (curr > left and curr < right):
            l = mid + 1
        elif (curr < left and curr > right):
            r = mid - 1
        else:  # both are less, we can go either way
            l = mid + 1
    return 0
def asc_order_binary_search(arr ,l, h, x):
    """

    :param arr:
    :param x:
    :return:
    """
    while l <= h:
        m = (h + l) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x:
            m -= 1
            h = m
        else:
            m += 1
            l = m
    else:
        return -1


def dsc_order_binary_search(arr ,l, h, x):
    """

    :param arr:
    :param x:
    :return:
    """
    while l <= h:
        m = l + (h - l // 2)
        if arr[m] == x:
            return m
        elif arr[m] < x:
            m -= 1
            h = m
        else:
            m += 1
            l = m
    else:
        return -1

def search(arr, x):
    """
    https://www.geeksforgeeks.org/find-element-bitonic-array/
    Given a bitonic sequence of n distinct elements, write a program to find a given element x in the bitonic sequence
    in O(log n) time. A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
    :param arr:
    :param x:
    :return:
    """
    max_index = max_ele_index(arr)
    if arr[max_index] == x:
        return max_index
    res = asc_order_binary_search(arr, max_index+1, len(arr) - 1, x)
    if res != -1:
        return res
    return dsc_order_binary_search(arr[0:max_index], 0, max_index -1, x)



arr = [-3, 9, 8, 20, 17, 5, 1]
x = 5
print(search(arr, x))