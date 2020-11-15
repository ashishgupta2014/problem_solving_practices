def binay_search_itr(arr, x):
    """
    Given a sorted array, find the element in the array which has minimum difference with the given number.
    :param arr:
    :param x:
    :return:
    """
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = l + (h - l // 2)
        if arr[m] == x:
            return arr[m]
        elif arr[m] > x:
            m -= 1
            h = m
        else:
            m += 1
            l = m
    if abs(arr[l] - x) >= abs(arr[h] - x):
        return arr[h]
    else:
        return arr[l]

arr = [1, 4, 8, 10, 15]
x = 12
print(binay_search_itr(arr, x))