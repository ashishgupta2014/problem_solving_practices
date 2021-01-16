w = [2, 5, 7]
v = [60, 100, 120]
c = 10
n = len(w)
dp = [[-1 for x in range(c + 1)] for y in range(n + 1)]
def knapsack_recursive(w, v, c, n):
    """
    recursive and memorization technique
    """
    if n == 0 or c == 0:
        return 0
    if dp[n][c] != -1:
        return dp[n][c]
    if w[n-1] <= c:
        dp[n][c] = max((v[n-1] + knapsack_recursive(w, v, c-w[n-1], n)), knapsack_recursive(w, v, c, n-1))
    else:
        dp[n][c] = knapsack_recursive(w, v, c, n-1)
    return dp[n][c]

print(knapsack_recursive(w, v, c, n))

def knapsack_top_down(w, v, c, n):
    """
    iterative and top down dp problem
    rod cutting problem is same
    """
    dp = [[0 for x in range(c + 1)] for x in range(n + 1)]

    for i in range(1, n+1):

        for j in range(1, c+1):
            if w[i-1] <= j:
                dp[i][j] = max(v[i - 1] + dp[i][j - w[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][c]

print(knapsack_top_down(w, v, c, n))