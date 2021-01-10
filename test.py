import numpy as np
def knapsack(Val, wt, W):
    """

    :param Val:
    :param wt:
    :param W:
    :return:
    """
    dp = np.zeros((len(wt), W+1), int)
    for i in range(0, len(wt)):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], Val[i] + dp[i - 1][j - wt[i]])
    print(dp)
val = [1, 2, 3]
wt = [4, 5, 1]
w = 4

knapsack(val, wt, w)