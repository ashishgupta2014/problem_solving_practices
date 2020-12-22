def count_subset_sum(ar, n, s):
    if (s == 0):
        return 1
    if (n == 0 and s != 0):
        return 0
    elif ar[n - 1] <= s:
        return count_subset_sum(ar, n - 1, s - ar[n - 1]) + count_subset_sum(ar, n - 1, s)
    else:
        return count_subset_sum(ar, n - 1, s)

ar = [2, 3, 5, 6, 8, 10]
n = 6
s = 10

print(count_subset_sum(ar, n, s))
dp = []
for i in range(n+1):
    a = []
    for j in range(s+1):
        if i == 0 and j == 0:
            a.append(1)
        elif i == 0:
            a.append(0)
        elif j == 0:
            a.append(1)
        else:
            a.append(0)
    dp.append(a)

def count_subset_sum_top_down(ar, n, s):
    for i in range(1, n+1):
        for j in range(1, s+1):
            if ar[i-1] <= j:
                dp[i][j] = dp[i-1][j - ar[i - 1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][s]
print(count_subset_sum_top_down(ar, n, s))