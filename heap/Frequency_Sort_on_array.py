from queue import PriorityQueue
from collections import Counter


def solve(arr):
    """
    Print the elements of an array in the increasing frequency if 2 numbers have same frequency then print the one which came first.

    Example:
    Input : arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
    Output : arr[] = {8, 8, 8, 2, 2, 5, 5, 6}
    :param arr:
    :param k:
    :return:
    """
    d = Counter(arr)
    pq = PriorityQueue()
    for key, value in d.items():
        pq.put((-value, key))
    while (not pq.empty()):
        value, key = pq.get()
        for i in range(abs(value)):
            print(key, end=' ')


if __name__ == '__main__':
    arr = [2, 5, 2, 8, 5, 6, 8, 8]
    solve(arr)