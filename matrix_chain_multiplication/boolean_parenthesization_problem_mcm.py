s = 'T|T&F^T'
d = dict()
def solve(s, i, j, is_true):
    """
    memoized version using map
    https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/

    T ^ T = False
    F ^ T = True
    T ^ F = True
    F ^ F = False
    _____________

    T & T = True
    F & T = False
    T & F = False
    F & F = False

    _____________

    T | T = True
    F | T = True
    T | F = True
    F | F = False

    :param s:
    :param i:
    :param j:
    :param is_true:
    :return:
    """
    if i > j:
        return False
    if i == j:
        if is_true:
            return s[i] == 'T'

        else:
           return s[i] == 'F'
    if d.get(str(i)+str(j)+str(is_true), None):
        return d[str(i)+str(j)+str(is_true)]

    ans = 0
    k = i+1
    while k <= j-1:
        lt = solve(s, i, k-1, True)
        lf = solve(s, i, k-1, False)
        rt = solve(s, k+1, j, True)
        rf = solve(s, k+1, j, False)
        if s[k] == '&':
            if is_true:
                ans += lt * rt
            else:
                ans += lt * rf + lf * rt + lf * rf
        elif s[k] == '|':
            if is_true:
                ans += lt * rf + lf * rt + lt * rt
            else:
                ans += lf * rf
        elif s[k] == '^':
            if is_true:
                ans += lt * rf + lf * rt
            else:
                ans += lf * rf + lt * rt
        d[str(i) + str(j) + str(is_true)] = ans
        k += 2
    return ans

print(solve(s, 0, len(s)-1, True))
print(d)
