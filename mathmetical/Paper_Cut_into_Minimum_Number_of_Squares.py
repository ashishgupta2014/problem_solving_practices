"""
https://app.glider.ai/practice/problem/algorithms/paper-cut/problem

Cut the paper of size A x B into squares of any size. Find the minimum number of squares that can be cut from the paper.

Input
The first line of input contains an integer A.
The second line of input contains an integer B.

Output
Print a minimum number of squares.

Constraints
1  <= A, B <= 100

Example #1
Input
13
29
Output
9
Explanation:  2 ( 13 x 13 ) + 4 ( 3 x 3) + 3 ( 1 x 1 ) = 9.

"""

MAX = 300
dp = [[0 for i in range(MAX)] for i in range(MAX)]


# Returns min number of squares needed


def minimumSquare(m, n):
    # Initializing max values to
    # vertical_min
    # and horizontal_min
    vertical_min = 10000000000
    horizontal_min = 10000000000

    # N=11 & M=13 is a special case
    if n == 13 and m == 11:
        return 6
    if m == 13 and n == 11:
        return 6

    # If the given rectangle is
    # already a square
    if m == n:
        return 1

    # If the answer for the given rectangle is
    # previously calculated return that answer
    if dp[m][n] != 0:
        return dp[m][n]

    # The rectangle is cut horizontally and
    # vertically into two parts and the cut
    # with minimum value is found for every
    # recursive call.
    for i in range(1, m // 2 + 1):
        # Calculating the minimum answer for the
        # rectangles with width equal to n and length
        # less than m for finding the cut point for
        # the minimum answer
        horizontal_min = min(minimumSquare(i, n) + minimumSquare(m - i, n), horizontal_min)
    for j in range(1, n // 2 + 1):
        # Calculating the minimum answer for the
        # rectangles with width equal to n and length
        # less than m for finding the cut point for
        # the minimum answer
        vertical_min = min(minimumSquare(m, j) + minimumSquare(m, n - j), vertical_min)

    # Minimum of the vertical cut or horizontal
    # cut to form a square is the answer
    dp[m][n] = min(vertical_min, horizontal_min)
    return dp[m][n]


def minimumSquare_approch2(a, b):
    result = 0

    # swap if a is small size side .
    if (a < b):
        a, b = b, a

    # Iterate until small size side is
    # greater then 0
    while (b > 0):
        # Update result
        result += int(a / b)

        rem = int(a % b)
        a = b
        b = rem

    return result


# Driver code
if __name__ == '__main__':
    m = 11
    n = 13

    # Function call
    print(minimumSquare(m, n))  ## write approch
    print(minimumSquare_approch2(m, n))  ## theory approch, most of places this approch works better
