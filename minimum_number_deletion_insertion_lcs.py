x = "heap"
y = "pea"

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
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][m]

def minimum_number_del_insert(x, y, n , m):
    """
    convert x to y with minimum number of insert or delete operation
    """
    lcs_len = lcs_top_down(x, y, n, m)
    print('LCS: ', lcs_len)
    print('Minimum delete: ', n - lcs_len)
    print('Minimum Insert: ', m - lcs_len)

minimum_number_del_insert(x, y, n , m)