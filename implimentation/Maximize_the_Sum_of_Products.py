from collections import deque
def solve(arr):
    """
    https://app.glider.ai/practice/problem/algorithms/maximize-the-sum-of-products/problem

    Given N positive integers, you are able to remove an element from either of the two ends, each time you remove an
    element, the score is increasing by the value of element * (number of elements removed + 1). You must find the
    maximum score that can be obtained by removing all the elements.

    Input
    The first line of input contains an integer N, representing the size of the array.
    The second line of input contains N space-separated integers, representing the array elements.

    Output
    A maximum score can be obtained by removing all the elements.

    :return:
    """
    s = 0
    index = 0
    while arr:
        if arr[0] > arr[-1]:
            s += arr[-1] * (index + 1)
            arr.pop()
        else:
            s += arr[0] * (index + 1)
            arr.popleft()
        index += 1
    return s
arr = deque(list(map(int, '1 3 1 5 2'.split())))
print(solve(arr))