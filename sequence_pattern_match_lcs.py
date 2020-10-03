x = "abac"
y = "cab"

n = len(x)
m = len(y)
def lcs_top_down(x, y, n, m):
    """
    Sequence pattern match among one of the string
    one of string fully contain another string return True otherwise False
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
                # if we want sub sequence of two string with break allowed
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    if min(n, m) == dp[n][m]:
        return True
    return False
print(lcs_top_down(x, y, n, m))