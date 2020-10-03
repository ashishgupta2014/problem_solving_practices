x = "abac"
y = "cab"

n = len(x)
m = len(y)
def lcs_top_down(x, y, n, m):
    """
    print super common sequence of two string
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
    out = ''
    i = n
    j = m
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            out += x[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                out += y[j-1]
                j -= 1
            else:
                out += x[i-1]
                i -= 1
    while i > 0:
        out += x[i-1]
        i -= 1
    while j > 0:
        out += y[j-1]
        j -= 1



    return out[::-1]
print(lcs_top_down(x, y, n, m))