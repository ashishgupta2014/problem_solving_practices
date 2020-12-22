"""
https://app.glider.ai/practice/problem/algorithms/number-of-squares-that-sum-to-n/problem

https://leetcode.com/problems/perfect-squares/

You are given a positive integer N. Print the minimum count of numbers in the square forms (x2​)​​​ needed, whose sum results in value N.

Input
The input contains an integer N.

Output
 Print the minimum number of squares that sum to N.

Constraints
1 <= N <= 105

Example #1
Input
24
Output
3
Explanation: 24 = 16 + 4 + 4, where 16 = 42​, 4 = 22​, 4 = 22​.​​​


https://leetcode.com/problems/perfect-squares/

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

from math import sqrt
def squareSum(n):
    """

    :param n:
    :return:
    """
    sqr = sqrt(n)
    pool = {i ** 2 for i in range(int(sqr) + 1)}
    test = [i ** 2 for i in range(int(sqr * 0.71) + 1)]

    for i in test:
        for j in test:
            if n - i - j in pool:
                return 3 - (i == 0) - (j == 0)
    return 4

print(squareSum(24))