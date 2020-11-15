arr = [10, 3, 0, 1, 6]

def insert(arr, ele):
    """

    :param arr:
    :param ele:
    :return:
    """
    n = len(arr)
    if n == 0 or arr[n-1] <= ele:
        arr.append(ele)
        return
    temp = arr.pop(n-1)
    insert(arr, ele)
    arr.append(temp)
    return

def rec_sort(arr):
    """

    :param arr:
    :param n:
    :return:
    """
    n = len(arr)
    if n == 1:
        return
    temp = arr.pop(n-1)
    rec_sort(arr)
    insert(arr, temp)

rec_sort(arr)
print(arr)