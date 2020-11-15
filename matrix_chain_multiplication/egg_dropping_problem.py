e = 2
f = 36
dp = []
for i in range(e+1):
    a = []
    for j in range(f + 1):
        a.append(-1)
    dp.append(a)

def solve(e, f):
    """
    https://www.includehelp.com/algorithms/egg-dropping-problem-using-dynamic-programming.aspx

    You are given N floor and K eggs. You have to minimize the number of times you have to drop the eggs to find the critical floor where critical floor means the floor beyond which eggs start to break. Assumptions of the problem:

    If egg breaks at ith floor then it also breaks at all greater floors.
    If egg does not break at ith floor then it does not break at all lower floors.
    Unbroken egg can be used again.
    Note: You have to find minimum trials required to find the critical floor not the critical floor.

    :param e: no of eggs
    :param f: no of floors
    :return:
    """
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f
    if dp[e][f] != -1:
        return dp[e][f]
    mn = float('inf')
    for k in range(1, f+1):
        if dp[e-1][k-1] != -1:
            low = dp[e-1][k-1]
        else:
            low = solve(e-1, k-1)
            dp[e-1][k-1] = low
        if dp[e][f-k] != -1:
            high = dp[e][f-k]
        else:
            high = solve(e, f-k)
            dp[e][f-k] = high
            
        temp = 1 + max(low, high)
        mn = min(temp, mn)
    dp[e][f] = mn
    return mn
print(solve(e, f))