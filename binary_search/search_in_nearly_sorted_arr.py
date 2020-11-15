def binay_search_itr(arr, x):
    """
    https://www.geeksforgeeks.org/search-almost-sorted-array/
    :param arr:
    :param x:
    :return:
    """
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = l + (h - l // 2)
        if arr[m] == x:
            return m
        if (m - 1) > l and arr[m - 1] == x:
            return m - 1
        if (m + 1) < h and arr[m + 1] == x:
            return m + 1
        elif arr[m] > x:
            m -= 2
            h = m
        else:
            m += 2
            l = m
    else:
        return -1
print(binay_search_itr([10, 3, 40, 20, 50, 80, 70], 40))