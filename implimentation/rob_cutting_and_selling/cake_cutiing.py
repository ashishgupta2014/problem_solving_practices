"""
https://app.glider.ai/practice/problem/algorithms/cake-cutting/problem

Given a big Cake of length N, We can cut the cake into different sized pieces & each cake piece has a different price based size, determine the maximum value obtainable by cutting up the cake and selling the pieces.

Input
The first line of input contains an integer N, denotes cake length.
The second line of input contains N space-separated integers, denoting the array elements as prices of each ith sized cake piece.

Output
The maximum value that can be obtained by cutting up the cake and selling the pieces.

Constraints
1 <= N <= 105

Example #1
Input
8
1 5 8 9 10 17 17 20
Output
22
Explanation: We can cut it into two pieces of lengths 2 and 6 (the cake piece of length 2 price is 5 + cake piece of length 6 price is 17, So 5+17 = 22).
Example #2
Input
8
3 5 8 9 10 17 17 20
Output
24
Explanation: We can cut it into eight pieces of length 1 ( the cake piece of length 1 price is 3, So 3x8 =24).
"""
import sys

INT_MIN = -sys.maxsize - 1
def cakeCut(price):
    n = len(price)
    if n <= 0:
        return 0
    val = [0 for _ in range(n + 1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]

arr = [1, 5, 8, 9, 10, 17, 17, 20]
print(cakeCut(arr))