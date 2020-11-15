string = 'ABC'
def solve(s, out):
    """
    https://practice.geeksforgeeks.org/problems/permutation-with-spaces/0
    print permutation with spaces
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
print(solve(string[1:], string[0]))

