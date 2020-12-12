import numpy as np
def lcs_top_down(string1, string2):
    """
    https://app.glider.ai/practice/problem/algorithms/subsequence-d-287976/problem
    longest printing common sequence
    You are given two strings str1 and str2. Both of them contain only lowercase Latin letters. You must check whether
    str1 is a subsequence of str2 or not.

    print matching length
    """
    n = len(string1)
    m = len(string2)
    dp = np.zeros([n+1, m+1], dtype=int)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                # if we want sub sequence of two string with break allowed
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][m]
print(lcs_top_down('a', 'bcd'))


def isSubSequence(str1, str2):
    """
    https://www.geeksforgeeks.org/given-two-strings-find-first-string-subsequence-second/

    https://app.glider.ai/practice/problem/algorithms/subsequence-d-287976/problem

    You are given two strings str1 and str2. Both of them contain only lowercase Latin letters.
    You must check whether str1 is a subsequence of str2 or not.
    :param str1:
    :param str2:
    :return:
    """
    m = len(str1)
    n = len(str2)

    j = 0  # Index of str1
    i = 0  # Index of str2

    # Traverse both str1 and str2
    # Compare current character of str2 with
    # first unmatched character of str1
    # If matched, then move ahead in str1

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1

    # If all characters of str1 matched, then j is equal to m
    return j == m

print(isSubSequence('a', 'bcd'))