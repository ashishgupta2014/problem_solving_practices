"""
https://www.geeksforgeeks.org/coin-change-dp-7/

Given a value N, if we want to make change for N cents, and we have infinite supply of each of
S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five
solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
"""

coins = [1, 2, 3]
s = 5
n = len(coins)
dp = []
for i in range(n+1):
    a = []
    for j in range(s + 1):
        if (i == 0 and j == 0) or j == 0:
            a.append(1)
        else:
            a.append(0)
    dp.append(a)
    
def knapsack_top_down(coins, s, n):
    """
    iterative and top down dp problem
    same as subset sum problem but has repetition of array elements allowed
    find number of ways coins sum == target sum
    """
    for i in range(1, n+1):
        for j in range(1, s+1):
            if coins[i-1] <= j:
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][s]

print(knapsack_top_down(coins, s, n))