def binay_search_itr(arr, x):
    """
    https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/

    Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x,
    and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing
    order. Write efficient functions to find floor and ceiling of x.

    Examples :

    For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
    For x = 0:    floor doesn't exist in array,  ceil  = 1
    For x = 1:    floor  = 1,  ceil  = 1
    For x = 5:    floor  = 2,  ceil  = 8
    For x = 20:   floor  = 19,  ceil doesn't exist in array
    In below methods, we have implemented only ceiling search functions. Floor search can be implemented in the same way.

    Method 1 (Linear Search)
    Algorithm to search ceiling of x:
    1) If x is smaller than or equal to the first element in array then return 0(index of first element)
    2) Else Linearly search for an index i such that x lies between arr[i] and arr[i+1].
    3) If we do not find an index i in step 2, then return -1

    :param arr:
    :param x:
    :return:
    """
    l = 0
    h = len(arr) - 1
    res = -1
    while l <= h:
        m = l + (h - l // 2)
        if arr[m] == x:
            return arr[m]
        elif arr[m] > x:
            res = arr[m]
            h = m - 1
        else:
            l = m + 1
    return res
print(binay_search_itr([1, 2, 8, 10, 10, 12, 19], 5))