"""
https://www.interviewbit.com/problems/find-duplicate-in-array/

Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than
O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
"""

class SolutionSpaceOptimized:
    # @param A : tuple of integers
    # @return an integer
    #
    def repeatedNumber(self, A):
        slow = A[0]
        fast = A[A[0]]

        while (slow != fast):
            slow = A[slow]
            fast = A[A[fast]]
        fast = 0

        while (slow != fast):
            slow = A[slow]
            fast = A[fast]
        return slow
arr = [3, 4, 1, 4, 3]
obj = SolutionSpaceOptimized()
print(obj.repeatedNumber(arr))

class SolutionTimeOptimized:
    # @param A : tuple of integers
    # @return an integer
    # uses extra n space but optimized as time
    def repeatedNumber(self, A):
        n=len(A)
        seen=[False]*n
        for x in A:
            if seen[x]==True:
                return x
            else:
                seen[x]=True
        return -1
arr = [3, 4, 1, 4, 3]
obj = SolutionTimeOptimized()
print(obj.repeatedNumber(arr))

from collections import Counter
class SolutionTimeOptimized2:
    # @param A : tuple of integers
    # @return an integer
    # uses extra n space but optimized as time
    def repeatedNumber(self, A):
        return Counter(A).most_common()[0][0]
arr = [3, 4, 1, 4, 3]
obj = SolutionTimeOptimized()
print(obj.repeatedNumber(arr))