string = 'ABC'
def solve(s, out):
    """
    https://www.geeksforgeeks.org/permute-string-changing-case/
    print string with case change combination
    :param s:
    :param out:
    :return:
    """
    if len(s) == 0:
        print(out)
        return
    a, b = out, out
    a += s[0]
    b += s[0].upper()
    solve(s[1:], a)
    solve(s[1:], b)
print(solve(string.lower(), ''))

