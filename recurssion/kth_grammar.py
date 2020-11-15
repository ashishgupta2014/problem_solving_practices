def solve(N, K):
    """
    https://leetcode.com/problems/k-th-symbol-in-grammar/
    :param N:
    :param K:
    :return:
    """
    if N == 1 or K == 1:
        return 0

    mid = (2 ** (N - 1)) // 2

    if K <= mid:
        return solve(N - 1, K)
    else:
        return int(not solve(N - 1, K - mid))
print(solve(4, 5))