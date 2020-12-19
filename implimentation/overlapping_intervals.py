from collections import deque


def solve(arr):
    """

    :param arr:
    :return:
    """
    arr.sort(key=lambda x: x[0])
    out = deque(arr)
    n = len(arr)
    i = 0
    while n > 0 and len(out) > 1:
        if len(out) - 1 > i and out[i][1] > out[i+1][0]:
            f = out.popleft()
            r = out.popleft()
            out.appendleft([f[0], max(f[1], r[1])])
        else:
            i += 1
        n -= 1

    return out
arr = [[1, 3], [2, 4], [6, 8], [9, 10]]
#arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
print(solve(arr))