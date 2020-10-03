arr = [10, 20,30,40,30]
dp = []
n = len(arr)
for i in range(n+1):
    a = []
    for j in range(n+1):
        a.append(-1)
    dp.append(a)

def solve(arr, i, j):
    """
    https://algorithmsandme.com/tag/leetcode-matrix-chain-multiplication/
    https://www.youtube.com/watch?v=kMK148J9qEE&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=34

    https://leetcode.com/problems/minimum-score-triangulation-of-polygon/submissions/
    :param arr:
    :param i:
    :param j:
    :return:
    """
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mn = float('inf')
    k = i
    while k <= j-1:
        temp = solve(arr, i, k) + solve(arr, k + 1, j) + arr[i-1] * arr[k] * arr[j]
        if temp < mn:
            mn = temp
        k += 1
    dp[i][j] = mn
    return mn
print(solve(arr, 1, n-1))
