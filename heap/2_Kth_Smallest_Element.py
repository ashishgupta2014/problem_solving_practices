from heapq import heappush, heappushpop
def solve(arr, k):
    """
    Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in
    the given array. It is given that all array elements are distinct.
    :param arr:
    :param k:
    :return:
    """
    smallest = []

    for value in arr:
        if (len(smallest) < k):
            heappush(smallest, -value)
        else:
            heappushpop(smallest, -value)
    if (len(smallest) < k):
        return None
    return -smallest[0]
arr = [1, 23, 12, 9, 30, 2, 50] # [1, 2, 9, 12, 23, 30, 50]
k = 4
print(solve(arr, k))
