coins = [1, 2, 3, 2, 1]
s = 10
n = len(coins)
dp = []
for i in range(n + 1):
    a = []
    for j in range(s + 1):
        if i == 0 or i == 1:
            if i == 1 and j != 0 and coins[i-1] % j == 0:
                a.append(1)
            else:
                a.append(float('inf') - 1)
        else:
            a.append(0)
    dp.append(a)


def knapsack_top_down(coins, s, n):
    """
    iterative and top down dp problem
    same as subset sum problem but has repetition of array elements allowed
   minimum number of coins used to get the target sum
    """
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][s]


print(knapsack_top_down(coins, s, n))