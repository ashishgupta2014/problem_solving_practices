from heapq import heappop, heappush, heapify

def solve(arr, k):
    """
    Using min_heap
    write an efficient program for printing k largest elements in an array. Elements in array can be in any order.

    For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3
    then your program should print 50, 30 and 23.
    :param arr:
    :param k:
    :return:
    """
    min_heap = [arr[0]]
    heapify(min_heap)
    for i in arr[1:]:
        heappush(min_heap, i)
        if len(min_heap) > k:
            heappop(min_heap)
    return min_heap
arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(solve(arr, k))
