"""
https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

You are given a few points on the coordinate plane and are asked to go through (or visit) all of the given points in
the same order as they are given in the input. You can move from a point to any one of its eight adjacent points and it
 will be counted as a single step. For a given point ( x, y ), its eight adjacent points are as follows:-

( x+1, y )

( x-1, y )

( x, y+1 )

( x, y-1 )

( x+1, y+1 )

( x-1, y+1 )

( x+1, y-1 )

( x-1, y-1 )

You have to visit all the given points in the same order taking the minimum number of steps. And to move from one
point to another in the minimum number of steps you need to go through a path that is the shortest amongst all. See the
 example below for better understanding of the problem.

Input:-

[0, 1, 1, 2]

[0, 0, 3, 4]

Given points in input are ( 0, 0 ) ( 1, 0 ) ( 1, 3 ) ( 2, 4 ). With these points what you are required to do is first
move from ( 0, 0 ) to ( 1, 0 ). It will take 1 step. Then move from ( 1, 0 ) to ( 1, 3 ). It will take 3 steps.
Then from ( 1, 3 ) to ( 2, 4 ). And it will take 1 step (moving diagonally to upper right point).

So the total steps taken will be 1+3+1.

Output: 5

Hint: The minimum number of steps to move from one point, say (x1, y1), to another point, say (x2, y2),
is maximum( abs(x2-x1), abs(y2-y1) ).
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        path_count = 0
        for i in range(1, len(A)):
            path_count += max(abs(A[i]-A[i-1]), abs(B[i]-B[i-1]))
        return path_count
obj = Solution()
print(obj.coverPoints(A=[0, 1, 1], B=[0, 1, 2]))