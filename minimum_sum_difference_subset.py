ar = [ 3, 1, 4, 2, 2, 1 ] 
def subset_sum(ar, n, s):
    dp = []
    for i in range(n+1):
        a = []
        for j in range(s+1):
            if (i == 0 and j == 0) or j == 0:
                a.append(True)
            elif i == 0:
                a.append(False)
            else:
                a.append(None)
        dp.append(a)
    for i in range(1, n+1):
        for j in range(1, s+1):
            if ar[i-1] <= j:
                dp[i][j] = dp[i-1][j-ar[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp
def minimum_sun_diff(ar):
    s = sum(ar)
    n = len(ar)
    dp = subset_sum(ar, n, s)
    for j in range(s // 2, -1, -1):
       if dp[n][j]:
           return s - (2 * j)
print(minimum_sun_diff(ar))