ar = [2, 3, 5, 6, 8, 10]
d = 1
def count_subset_sum_top_down(ar, n, s):
    dp = []
    for i in range(n + 1):
        a = []
        for j in range(s + 1):
            if (i == 0 and j == 0) or j == 0:
                a.append(1)
            else:
                a.append(0)
        dp.append(a)
    for i in range(1, n+1):
        for j in range(1, s+1):
            if ar[i-1] <= j:
                dp[i][j] = dp[i-1][j - ar[i - 1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][s]

def subset_sum_given_diff(ar, d):
    n = len(ar)
    s = sum(ar)
    s1 = (s + d) // 2
    return count_subset_sum_top_down(ar, n, s1)
print(subset_sum_given_diff(ar, d))