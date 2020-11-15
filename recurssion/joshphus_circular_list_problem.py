def solve(arr, index, k):
    """
    https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle/0
    :param arr:
    :param k:
    :return:
    """
    if len(arr) == 1:
        return arr
    i = (index + k) % len(arr)
    arr.pop(i)
    solve(arr, i, k)
n = 5
k = 2
arr = [i for i in range(1, n+1)]
solve(arr, 0, k - 1)
print(arr[0])