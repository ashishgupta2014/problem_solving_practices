"""
https://app.glider.ai/practice/problem/algorithms/pair-with-given-difference--binary-search-/problem

https://discuss.interviewbit.com/t/python-3-simple-pointer-approach/57049

For a given array and difference K, find if there exists a pair of elements in the array with difference K.

Input
The first line of input contains an integer N, representing the size of the array.
The second line of input contains N space-separated integers, representing the array elements.
The third line of input contains an integer K, representing the difference value.

Output
Print space-separated two integers if the difference exists, print -1 otherwise.

Constraints
0 <= N <= 105
-104 <= K <= 104

Example #1
Input
6
4 50 2 -40 80 1
120
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        """

        :param A:
        :param B:
        :return:
        """
        A.sort()
        B = abs(B)
        i = 0
        j = 1
        while j < len(A):
            if A[j]-A[i]-B == 0:
                return A[i], A[j]
            elif A[j]-A[i]-B > 0:
                i += 1
                if i == j:
                    j += 1
            else:
                j += 1
        return -1
obj = Solution()
print(obj.solve([4, 50, 2, -40, 80, 1], 120))