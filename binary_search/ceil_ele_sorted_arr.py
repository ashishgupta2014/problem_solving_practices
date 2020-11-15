def binay_search_itr(arr, x):
    """
    https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
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