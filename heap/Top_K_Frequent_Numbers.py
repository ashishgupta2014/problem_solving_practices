from queue import PriorityQueue
from collections import Counter


def solve(arr, k):
    """
   Given an array of n numbers. Your task is to read numbers from the array and keep at-most K numbers at the top
   (According to their decreasing frequency) every time a new number is read. We basically need to print top k numbers
   sorted by frequency when input stream has included k distinct elements, else need to print all distinct elements
   sorted by frequency.

    Example:
    Input :  arr[] = {5, 2, 1, 3, 2}
    k = 4
    Output : 5 2 5 1 2 5 1 2 3 5 2 1 3 5
    :param arr:
    :param k:
    :return:
    """
    d = Counter(arr)
    pq = PriorityQueue()
    i = 0
    for key, value in d.items():
        pq.put((value, key))
        i += 1
        if i == k:
            pq.get()
            i = 0
    while (not pq.empty()):
        p, q = pq.get()
        print(f'Frequency: {p} Key: {q}')


if __name__ == '__main__':
    arr = [5, 2, 1, 3, 2, 1, 1, 5, 5, 5]
    k = 2
    solve(arr, k)