"""
https://www.interviewbit.com/problems/first-missing-integer/

Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
"""

from collections import Counter
class SolutionUsingDict:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        d = Counter(A)
        m = max(A)
        if m > 0:
            for i in range(1,m):
                if d.get(i, None):
                    continue
                else:
                    return i
            return m+1
        return 1
arr = [1,2,0]
obj = SolutionUsingDict()
print(obj.firstMissingPositive(arr))


class SolutionOptimized1:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):

        if len(A) == 0:
            return 1

        maxpos = max(A) + 1

        for i in range(len(A)):
            if A[i] <= 0:
                A[i] = maxpos

        A.sort()

        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1

        return maxpos
arr = [1,2,0]
obj = SolutionOptimized1()
print(obj.firstMissingPositive(arr))

class SolutionOptimized2:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A = list(filter(lambda x : x > 0, A))
        A.sort()
        for i in range(len(A)):
            if(A[i]!=i+1):
                return i+1
        return len(A)+1
arr = [1,2,0]
obj = SolutionOptimized2()
print(obj.firstMissingPositive(arr))


