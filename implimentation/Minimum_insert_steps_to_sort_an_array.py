def minSteps(arr):
    """
    https://www.geeksforgeeks.org/minimum-insertions-sort-array/

    https://app.glider.ai/practice/problem/algorithms/minimum-steps-to-sort-an-array/problem

    Minimum insertions to sort an array

    You are given an array consisting of N integers. You must sort this array in a minimum number of steps.
    In one step you can insert any array element from its position to any other position.
    Print the minimum number of steps required to sort the array.

    Input
    The first line of input contains an integer N, representing the size of the array.
    The second line of input contains N space-separated integers, representing the array elements.

    Output
    Print a minimum number of steps.


    :param arr:
    :return:
    """
    N = len(arr)
    # lis[i] is going to store length
    # of lis that ends with i.
    lis = [0] * N

    # Initialize lis values for all indexes
    for i in range(N):
        lis[i] = 1

    # Compute optimized lis values in
    # bottom up manner
    for i in range(1, N):
        for j in range(i):
            if (arr[i] >= arr[j] and
                    lis[i] < lis[j] + 1):
                lis[i] = lis[j] + 1

    # The overall LIS must end with of the array
    # elements. Pick maximum of all lis values
    max = 0
    for i in range(N):
        if (max < lis[i]):
            max = lis[i]

            # return size of array minus length
    # of LIS as final result
    return (N - max)
print(minSteps(list(map(int, '7 45 4 8 56 8 5 9'.split()))))