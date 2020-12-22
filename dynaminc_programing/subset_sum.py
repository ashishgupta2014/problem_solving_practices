from functools import lru_cache
ar = [3, 34, 4, 12, 5, 2]
n = 6
s = 9
dp = []
for i in range(n+1):
    a = []
    for j in range(s+1):
        if i == 0 and j == 0:
            a.append(True)
        elif i == 0:
            a.append(False)
        elif j == 0:
            a.append(True)
        else:
            a.append(None)
    dp.append(a)

def pair_presence(ar, n, s):
    if (s == 0):
        return True
    if (n == 0 and s != 0):
        return False
    elif ar[n-1] <= s:
        return pair_presence(ar, n-1, s-ar[n-1]) or pair_presence(ar, n-1, s)
    else:
        return pair_presence(ar, n-1, s)

print(pair_presence(ar, n, s))

def pair_presence_top_down(ar, n, s):
    for i in range(1, n+1):
        for j in range(1, s+1):
            if ar[i-1] <= j:
                dp[i][j] = dp[i-1][j - ar[i - 1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][s]
print(pair_presence_top_down(ar, n, s))