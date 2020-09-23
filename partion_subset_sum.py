
ar = [1, 5, 5, 11]
n = 4

def pair_presence_top_down(ar, n, s):
    dp = []
    for i in range(n + 1):
        a = []
        for j in range(s + 1):
            if i == 0 and j == 0:
                a.append(True)
            elif i == 0:
                a.append(False)
            elif j == 0:
                a.append(True)
            else:
                a.append(None)
        dp.append(a)

    for i in range(1, n+1):
        for j in range(1, s+1):
            if ar[i-1] <= j:
                dp[i][j] = dp[i-1][j - ar[i - 1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][s]

def partion_subset_sum(ar, n):
    s = sum(ar)
    if s % 2 != 0:
        return False
    return pair_presence_top_down(ar, n, s=s // 2)
print(partion_subset_sum(ar, n))