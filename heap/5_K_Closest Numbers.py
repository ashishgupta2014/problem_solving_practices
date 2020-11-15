from queue import PriorityQueue


def printKclosest(arr, n, x, k):
    """
    Given an unsorted array and two numbers x and k, find k closest values to x.
    Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3
    :param arr:
    :param n:
    :param x:
    :param k:
    :return:
    """
    # Make a max heap of difference with
    # first k elements.
    pq = PriorityQueue()
    for i in range(k):
        pq.put((-abs(arr[i] - x), i))

        # Now process remaining elements
    for i in range(k, n):
        diff = abs(arr[i] - x)
        p, pi = pq.get()
        curr = -p

        # If difference with current
        # element is more than root,
        # then put it back.
        if diff > curr:
            pq.put((-curr, pi))
            continue
        else:

            # Else remove root and insert
            pq.put((-diff, i))

            # Print contents of heap.
    while (not pq.empty()):
        p, q = pq.get()
        print("{} ".format(arr[q]), end="")

    # Driver program to test above functions


if __name__ == '__main__':
    arr = [-10, -50, 20, 17, 80]
    x, k = 20, 2
    n = len(arr)
    printKclosest(arr, n, x, k)