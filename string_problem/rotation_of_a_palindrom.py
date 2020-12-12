def isPalindrome(string):
    """

    :param string:
    :return:
    """
    return string == string[::-1]
def solve(n, string):
    """
    https://app.glider.ai/practice/problem/algorithms/rotation-of-a-palindrom/problem

    https://www.geeksforgeeks.org/check-given-string-rotation-palindrome/

    You are given a string consisting of n lowercase Latin letters. Print "YES" (without quotes)
    if the given string is a clockwise rotation of a palindrome, print "NO" (without quotes) otherwise.
    :param n:
    :param string:
    :return:
    """
    if isPalindrome(string):
       return 'YES'
    n = len(string)
    for i in range(n-1):
        str1 = string[i + 1:n]
        str2 = string[0:i + 1]
        if isPalindrome(str1 + str2):
            return 'YES'
    return 'NO'


string = 'xxy'
n = len(string)
print(solve(n, string))