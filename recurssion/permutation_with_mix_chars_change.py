string = 'a1B2'
def solve(s, out, ans=set()):
    """
    https://leetcode.com/problems/letter-case-permutation/submissions/
    print permutation of string by changing chase of mix chars
    :param s:
    :param out:
    :return:
    """
    if len(s) == 0:
        ans.add(out)
        return
    a, b = out, out
    if not s[0].isnumeric():
        a += s[0].lower()
        b += s[0].upper()
    else:
        a += s[0]
        b += s[0]
    solve(s[1:], a, ans)
    solve(s[1:], b, ans)
    return ans

print(solve(string, ''))

