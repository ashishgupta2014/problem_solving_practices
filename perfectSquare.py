import math
def perfectSquare(n):
    if (n < 3): return n
    square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for square in square_nums:
            if (i < square): break
            dp[i] = min(dp[i], dp[i - square] + 1)  # +1 is for that square we are substracting.
    return dp[-1]
print(perfectSquare(12))