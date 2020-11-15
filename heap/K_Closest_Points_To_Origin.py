from heapdict import heapdict
def solve(arr, k):
    """
    Given a list of points on the 2-D plane and an integer K. The task is to find K closest points to the origin and print them.

    Note: The distance between two points on a plane is the Euclidean distance.

    Example:
    Input : point = [[3, 3], [5, -1], [-2, 4]], K = 2
    :param arr:
    :param k:
    :return:
    """
    min_dict_heap = heapdict()
    for x, y in arr:
        key = x**2 + y**2
        value = (x, y)
        min_dict_heap[-key] = value

    print(min_dict_heap.d)
    for i in range(k):
        print(min_dict_heap.popitem())

point = [[3, 3], [5, -1], [-2, 4]]
K = 2
solve(point, K)