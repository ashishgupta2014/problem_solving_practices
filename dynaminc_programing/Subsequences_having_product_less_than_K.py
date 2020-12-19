import numpy as np
def product(arr, K):
    """

    :param arr:
    :param K:
    :return:
    """
    lists = [[]]
    count = 0
    for i in range(len(arr)):
        orig = lists[:]
        new = arr[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
            result1 = np.prod(lists[j])
            if result1 < K:
                count += 1
        lists = orig + lists
    print(lists)
    print(count)
arr = list(map(int, '1 2 3 4'.split()))
product(arr, 10)