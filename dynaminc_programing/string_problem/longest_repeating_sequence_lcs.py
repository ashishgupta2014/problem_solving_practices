x = "aabcebdd"

n = len(x)
def lcs_top_down(x, n):
    """
    longest repeating sequences basis on LCS
    find the length of longest repeating sequence
    """
    y = x
    dp = []
    m = n

    for i in range(n+1):
        a = []
        for j in range(m+1):
            a.append(0)
        dp.append(a)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1] and i !=j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                # if we want sub sequence of two string with break allowed
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][m]
print(lcs_top_down(x, n))