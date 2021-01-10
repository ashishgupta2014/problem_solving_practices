"""
https://www.interviewbit.com/problems/repeat-and-missing-number-array/

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3]

Output:[3, 4]

A = 3, B = 4
"""


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        x = sum(A) - sum(set(A))
        k = sum(A) - int(n * (n + 1) / 2)

        return [x, x - k]
arr = [3, 1, 2, 5, 3]
obj = Solution()
print(obj.repeatedNumber(arr))


class Solution2:
    # @param A : tuple of integers
    # @return a list of integers

    def repeatedNumber(self, A):
        n = len(A)

        S = sum(A)
        Sn = (n * (n + 1)) // 2

        S2 = 0
        for num in A:
            S2 += num * num

        S2n = (n * (n + 1) * (2 * n + 1)) // 6

        diff = S - Sn
        summation = (S2 - S2n) // diff

        D = (summation - diff) // 2
        R = summation - D

        return [R, D]
arr = [3, 1, 2, 5, 3]
obj = Solution2()
print(obj.repeatedNumber(arr))

class Solution3:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        size = len(A) + 1
        count = [0] * size

        for val in A:
            count[val] += 1

            res1 = 0
            res2 = 0

        for idx, val in enumerate(count):
            if val == 2:
                res1 = idx
            if val == 0:
                res2 = idx

        return res1, res2
arr = [3, 1, 2, 5, 3]
obj = Solution3()
print(obj.repeatedNumber(arr))


