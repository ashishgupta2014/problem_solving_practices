res = []
def solve(n, one, zero, op):
    """
    https://www.geeksforgeeks.org/print-n-bit-binary-numbers-1s-0s-prefixes/
    :param n
    :param one:
    :param zero:
    :param op:
    :return:
    """
    if n == 0:
        res.append(op)
        return
    op1 = op
    op1 += '1'
    solve(n - 1, one + 1, zero, op1)
    if one > zero:
        op2 = op
        op2 += '0'
        solve(n - 1, one, zero + 1, op2)
    return
solve(4, 0, 0, '')
print(res)