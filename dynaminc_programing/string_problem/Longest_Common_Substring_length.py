import numpy as np

def lcs(x,y):
    """
    https://app.glider.ai/tutorials/longest-common-substring/problem

    Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
    Examples :
    Input : X = "Thisisadoll", y = "Thiswasaball"
    Output : 4, The longest common substring is "This" and is of length 4.

    Input : X = "abcdxyz", y = "xyzabcd"
    Output : 4, The longest common substring is "abcd" and is of length 4.

    Input : X = "zxabcdezy", y = "yzabcdezx"
    Output : 6, The longest common substring is "abcdez" and is of length 6.

    Input
    The first line of input contains a string X.
    The second line of input contains a string Y.

    Output
    Print the length of the longest common substring of the two strings.

    Constraints
    1<=size of X,size of Y<=100
    :param x:
    :param y:
    :return:
    """
    n = len(x) + 1
    m = len(y) + 1
    dp = np.zeros((n, m), dtype=int)
    result = 0
    for i in range(1, n):
        for j in range(1, m):
            if x[i-1] == y[j-1]:  # find only matching string only, result length will be without any break continuos length
                dp[i][j] = 1 + dp[i-1][j-1]
                result = max(dp[i][j], result)
    print(dp)
    return result
X = 'ABCDGH'
Y = 'ACDGHR'

print(lcs(X, Y))


