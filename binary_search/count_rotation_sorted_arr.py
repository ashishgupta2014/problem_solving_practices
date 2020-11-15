def solve(arr):
    """
    https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
    :param arr:
    :return:
    """
    l = 0
    n = len(arr)
    h = n - 1
    if arr[l] < arr[h]:
        return -1
    while l <= h:
        m = (l + h) // 2
        nxt = (m + 1) % n  # rotate index of the array from the last
        pre = (m + n - 1) % n  # rotate index of the array from the first
        if arr[nxt] > arr[m] and arr[pre] > arr[m]:
            return m
        elif arr[l] <= arr[m]:
            l = m + 1
        elif arr[m] <= arr[h]:
            h = m - 1
    return -1
arr = [4,5,6,7,0,1,2]
print(solve(arr))