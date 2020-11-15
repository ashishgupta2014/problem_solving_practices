res = []
def solve(open, closed, op):
    """
    https://www.interviewbit.com/problems/generate-all-parentheses-ii/
    :param open:
    :param closed:
    :param op:
    :return:
    """
    if open == closed == 0:
        res.append(op)
        return
    if open != 0:
        op1 = op
        op1 += '('
        solve(open - 1, closed, op1)
    if closed > open:
        op2 = op
        op2 += ')'
        solve(open, closed -1, op2)
    return
solve(2, 3, '(')
print(res)
