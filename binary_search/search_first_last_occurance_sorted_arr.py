def binary_search_first_occurrence(arr, x):
    """
    https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/
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
            res = m
            h = m - 1
        elif arr[m] > x:
            m -= 1
            h = m
        else:
            m += 1
            l = m
    return res

def binary_search_last_occurrence(arr, x):
    """
    https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/
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
            res = m
            l = m + 1
        elif arr[m] > x:
            m -= 1
            h = m
        else:
            m += 1
            l = m
    return res
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(f'First occurrence: {binary_search_first_occurrence(arr, x)}')
print(f'Last occurrence: {binary_search_last_occurrence(arr, x)}')
