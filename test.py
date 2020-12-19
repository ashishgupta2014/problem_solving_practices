def solve(arr, k):
    """

    :param arr:
    :param k
    :return:
    """
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == k:
            return m
        if arr[l] == k:
            return l
        if arr[h] == k:
            return h
        if arr[m] > arr[l] and arr[m] < k:
            l = m + 1
        elif arr[m] < arr[h] and arr[m] > k:
            h = m - 1
    return -1

arr = list(map(int, '9 3 15 29 31 31 32 '.split()))
k = 31
arr = [10, 3, 40, 20, 50, 80, 70]
k =  100
print(solve(arr, k))





