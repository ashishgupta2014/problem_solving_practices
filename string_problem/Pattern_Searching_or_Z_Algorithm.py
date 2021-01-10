def search(S, P):
    """
    https://app.glider.ai/practice/problem/algorithms/pattern-searching--z-algorithm-/problem
    
    For a given string S and pattern P, find all occurrences of P in S in linear time.

    Input
    The first line of input contains a string S.
    The second line of input contains a string P.

    Output
    Print the indices of all occurrences of P in S, print "-1" otherwise.

    Constraints
    1 <= length of S & P <= 104

    Example #1
    Input
    abc_abc_abc_abc
    abc
    :param S:
    :param P:
    :return:
    """
    i = 0
    n = len(P)
    out = []
    while i < len(S):
        if P[0] == S[i] and S[i:i+n] == P:
            out.append(i)
            i += n
        else:
            i += 1
    return out if out else [-1]
print(search('abc_abc_abc_abc', 'abc'))