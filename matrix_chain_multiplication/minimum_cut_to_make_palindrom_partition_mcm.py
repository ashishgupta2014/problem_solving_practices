s = 'ababbbabbababa'
dp = []
n = len(s)
for i in range(n+1):
    a = []
    for j in range(n+1):
        a.append(-1)
    dp.append(a)

def solve(s, i, j):
    """
    https://leetcode.com/problems/palindrome-partitioning-ii/
    https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/
    :param s:
    :param i:
    :param j:
    :return:
    """
    if i >= j or s[i:j+1][::-1] == s[i:j+1]:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mn = float('inf')
    k = i
    while k <= j - 1:
        if dp[i][k] != -1:
            left = dp[i][k]
        else:
            left = solve(s, i, k)
            dp[i][k] = left

        if dp[k + 1][j] != -1:
            right = dp[k + 1][j]
        else:
            right = solve(s, k + 1, j)
            dp[k + 1][j] = right
        temp = 1 + left + right
        if temp < mn:
            mn = temp
        k += 1
    dp[i][j] = mn
    return mn
print(solve(s, 0, n-1))

