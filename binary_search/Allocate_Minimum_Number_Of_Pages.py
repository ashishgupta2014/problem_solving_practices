def is_valid(arr, k, dist):
    """

    :param arr:
    :param k:
    :param dist:
    :return:
    """
    std = 1
    s = 0
    for i in arr:
        s += i
        if dist < s:
            s = i
            std += 1
        if std > k:
            return False
    return True


def mini_no_pages(arr, k):
    """
    https://www.geeksforgeeks.org/allocate-minimum-number-pages/

    Given number of pages in n different books and m students. The books are arranged in ascending order of number of
    pages. Every student is assigned to read some consecutive books. The task is to assign books in such a way that the
    maximum number of pages assigned to a student is minimum.

    :param arr:
    :param k:
    :return:
    """
    start = max(arr)
    end = sum(arr)
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if is_valid(arr, k, mid):
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res

arr = [12, 34, 67, 90]
k = 2
print(mini_no_pages(arr, k))
