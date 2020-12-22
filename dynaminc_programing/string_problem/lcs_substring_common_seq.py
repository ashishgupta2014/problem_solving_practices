x = "AGGTXB"
y = "GXTXAXB"

n = len(x)
m = len(y)
dp = []

def lcs_top_down(x, y, n, m):
    """
    "continuous sub sequence string"
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
                # if we want only longest continuous sub sequence of two string
                dp[i][j] = 0
    print(dp)
    return dp[n][m]
print(lcs_top_down(x, y, n, m))