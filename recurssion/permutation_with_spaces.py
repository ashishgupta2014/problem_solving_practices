string = 'ABC'
def solve(s, out):
    """
    https://practice.geeksforgeeks.org/problems/permutation-with-spaces/0

    https://app.glider.ai/tutorials/print-all-possible-strings-separated-by-a-space/problem
    print permutation with spaces

    Given a string S, you need to print all possible strings that can be made by placing spaces (zero or one)
    in between them.
    The output should be printed in sorted increasing order of strings.
    For Example:
    Input:  str[] = "ABC"
    Output: (A B C)(A BC)(AB C)(ABC)

    Input
    The input contains a string S of length  N.

    Output
    Print the string having all possible strings enclosed with ().

    Note: The output should be printed in sorted order.

    Constraints
    1<=length of S <=10

    Example #1
    Input
    AB
    Output
    (A B)(AB)
    :param s:
    :param out:
    :return:
    """
    if len(s) == 0:
        print(out)
        return
    a, b = out, out
    a += s[0]
    b += ' ' + s[0]
    solve(s[1:], a)
    solve(s[1:], b)
solve(string[1:], string[0])




