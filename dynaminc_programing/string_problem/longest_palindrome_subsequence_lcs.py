x = "agbcba"

n = len(x)

def lps_top_down(x, n):
    """
    longest palindrome sub sequence
    find the length
    LPS == reverse of first and then find lcs
    """
    y = x[::-1]
    print(y)
    m = n
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
    return dp[n][m]

print(lps_top_down(x, n))

def minimum_delete_to_convert_palindrome(x, n):
    """
    delete minimum number of chars to convert string as palindrome
    :param x:
    :param n:
    :return:
    """
    y = x[::-1]
    m = n
    dp = []
    for i in range(n + 1):
        a = []
        for j in range(m + 1):
            a.append(0)
        dp.append(a)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # if we want sub sequence of two string with break allowed
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return n - dp[n][m]
print(minimum_delete_to_convert_palindrome(x, n))


def minimum_insert_to_convert_palindrome(x, n):
    """
    minimum number insert of chars to convert string as palindrome
    :param x:
    :param n:
    :return:
    """
    y = x[::-1]
    m = n
    dp = []
    for i in range(n + 1):
        a = []
        for j in range(m + 1):
            a.append(0)
        dp.append(a)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # if we want sub sequence of two string with break allowed
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return m - dp[n][m]
print(minimum_insert_to_convert_palindrome(x, n))

