# unusul string sorting 
MAX = 26


# Function for alternate
# sorting of string 
def alternateSort(s):
    """
    https://www.geeksforgeeks.org/alternate-lower-upper-string-sort/

    https://app.glider.ai/practice/problem/algorithms/lower-upper-string-sort/problem

    Sort the given string S with a length of N, such that the uppercase and lowercase letter come in an alternate manner but in a sorted way.

    Input
    The input contains a string S.

    Output
    Print the sorted string.

    Constraints
    1 <= N <= 105
    :param s:
    :return:
    """
    n = len(s)

    # Count occurrences of
    # individual lower case and
    # upper case characters
    lCount = [0]*MAX
    uCount = lCount.copy()
    s = list(s)

    for i in range(n):
        if s[i].isupper():
            uCount[ord(s[i]) - ord('A')] += 1
        else:
            lCount[ord(s[i]) - ord('a')] += 1

    # Traverse through count
    # arrays and one by one
    # pick characters. Below
    # loop takes O(n) time
    # considering the MAX
    # is constant.
    i = 0
    j = 0
    k = 0

    while k < n:
        while i < MAX and uCount[i] == 0:
            i += 1
        if i < MAX:
            s[k] = chr(ord('A') + i)
            k += 1
            uCount[i] -= 1
        while j < MAX and lCount[j] == 0:
            j += 1
        if j < MAX:
            s[k] = chr(ord('a') + j)
            k += 1
            lCount[j] -= 1

    return "".join(s)


# Driver code
str = "KingDavidTheBuilder"
print(alternateSort(str))