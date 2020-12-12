def divide(arr):
    """
    https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1#

    https://app.glider.ai/practice/problem/algorithms/inversion-of-array/problem
    :param arr:
    :return:
    """
    n = len(arr) // 2
    if len(arr) == 1:
        return arr, 0
    left = arr[:n]
    right = arr[n:]
    left, left_count = divide(left)
    right, right_count = divide(right)
    count = left_count + right_count
    return merge(left, right, count)


def merge(left, right, count):
    arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr.append(right[j])
            j += 1
            count += 1
        elif left[i] == right[j]:
            arr.append(left[i])
            arr.append(right[j])
            i += 1
            j += 1
        else:
            arr.append(left[i])
            i += 1
    arr += right[j:]
    arr += left[i:]
    return arr, count

#arr = list(map(int, '2 4 1 3 5'.split()))
arr = [1, 20, 6, 4, 5]
print(divide(arr))