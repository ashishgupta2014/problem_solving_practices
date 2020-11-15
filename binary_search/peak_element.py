def binay_search_itr(arr):
    """
    https://leetcode.com/problems/find-peak-element/
    A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.


FIND MAXIMUM ELEMENT IN AN BITONIC ARRAY:

    :param arr:
    :param x:
    :return:
    """
    l = 0
    h = len(arr) - 1
    n = h
    while l <= h:
        m = l + (h - l // 2)

        if 0 < m > n:
            if arr[m - 1] > arr[m] < arr[m + 1]:
                return m
            elif arr[m] < arr[m - 1]:
                h = m - 1
            else:
                l = m + 1
        else:
            if m == 0:
                if arr[m] > arr[m + 1]:
                    return m
                else:
                    return m + 1
            if m == n:
                if arr[m] > arr[m - 1]:
                    return m
                else:
                    return m - 1

    else:
        return -1
arr = [1,2,3,1]
print(binay_search_itr(arr))