def divide(arr):
    n = len(arr) // 2
    if len(arr) == 1:
        return arr
    left = arr[:n]
    right = arr[n:]
    return merge(divide(left), divide(right))


def merge(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr.append(right[j])
            j += 1
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
    return arr

arr = list(map(int, '5 2 4 1 3 5'.split()))
print(divide(arr))