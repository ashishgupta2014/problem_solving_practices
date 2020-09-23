import numpy
def numberOfPaths(m, n):
    dp = numpy.empty((m + 1, n + 1))
    dp.fill(0)
    r = m+1
    c = n+1
    def cal(m, n):
        try:
            if m == 1 or n == 1:
                return 1
            elif r > m and c > n and dp[m][n] > 0:
                return dp[m][n]
            elif r > n and c > n and dp[n][m] > 0:
                return dp[n][m]
            else:
                dp[m][n] = cal(m - 1, n) + cal(m, n - 1)
        except Exception as e:
            dp[m][n] = cal(m - 1, n) + cal(m, n - 1)
        return dp[m][n]

    return cal(m, n)
print(numberOfPaths(23,12))