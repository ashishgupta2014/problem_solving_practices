def height(arr, K):
    """
    https://app.glider.ai/tutorials/minimize-the-heights/problem

    https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/

    Given an array, A denoting heights of N towers and a positive integer K, modify the heights of each tower either by
    increasing or decreasing them by K only once and then find out the minimum difference of the heights of the shortest
    and longest towers.
    Example:
    Input  : ar[] = {1, 15, 10}, k = 6
    Output : 5
    Explanation : We change 1 to 7, 15 to 9 and 10 to 4.
    Maximum difference is 5 (between 4 and 9). We can't get a lower difference.

    Input
    The first line of input contains an integer N, denoting the number of towers.
    The second line of input contains N space-separated integers denoting the heights of N towers.
    The third line of input contains an integer K, as described in the problem statement.

    Output
    Print out the minimum difference of heights possible.

    Constraints
    0 < K <= 30
    0 < N <= 30
    0 <= ar[i] <= 500`
    :param arr:
    :param K:
    :return:
    """
    arr.sort()
    n = len(arr)
    ans = arr[n - 1] - arr[0]
    small = arr[0] + K
    big = arr[n - 1] - K
    if small > big:
        small, big = big, small
    for i in arr[1:]:
        subtract = i - K
        add = i + K
        # If both subtraction and addition
        # do not change diff
        if (subtract >= small or add <= big):
            continue

        # Either subtraction causes a smaller
        # number or addition causes a greater
        # number. Update small or big using
        # greedy approach (If big - subtract
        # causes smaller diff, update small
        # Else update big)
        if (big - subtract <= add - small):
            small = subtract
        else:
            big = add
    return min(ans, big-small)
print(height([1,5, 8, 10], 2))