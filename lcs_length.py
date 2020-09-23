x = "AGGTAB"
y = "GXTXAYB"

n = len(x)
m = len(y)
dp = []
for i in range(n+1):
    a = []
    for j in range(m+1):
        a.append(-1)
    dp.append(a)


def lcs(x, y, n, m):
    """
    bottom up and memoization
    calculate length of longest substring can  be formed using two strings
    """
    if n == 0 or m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if x[n-1] == y[m-1]:
        dp[n][m] = 1 + lcs(x, y, n-1, m-1)
    else:
        dp[n][m] = max(lcs(x, y, n, m - 1), lcs(x, y, n - 1, m))
    return dp[n][m]

print(lcs(x, y, n, m))
print(dp)


def lcs_top_down(x, y, n, m):
    """

    """
    dp = []
    for i in range(n+1):
        a = []
        for j in range(m+1):
            a.append(0)
        dp.append(a)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp)
    return dp[n][m]
print(lcs_top_down(x, y, n, m))