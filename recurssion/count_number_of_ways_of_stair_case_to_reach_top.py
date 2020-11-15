def stepPerms(n):
    dp = [0] * max((n + 1), 4)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]
if __name__ == '__main__':
    print(stepPerms(2))