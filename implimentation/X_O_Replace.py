"""
https://app.glider.ai/practice/problem/algorithms/replace-os-with-xs/problem

Given a matrix of size N x M where every element is either ‘O’ or ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’. A ‘O’
(or a set of ‘O’) is considered to be by surrounded by ‘X’ if there are ‘X’ at locations just below, just above, just
left and just right of it.
Examples:
Input: mat[N][M] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'O', 'X'},
                     {'X', 'X', 'X', 'O', 'O', 'X'},
                     {'O', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                     {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
Output: mat[N][M] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'X', 'X', 'X'},
                      {'O', 'X', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'O', 'X', 'O'},
                      {'O', 'O', 'X', 'O', 'O', 'O'},
                     };
Input: mat[N][M] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'O', 'O', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };
Input: mat[N][M] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };

"""


# Python3 program to replace all 'O's with
# 'X's if surrounded by 'X'

# Size of given matrix is M x N

# A recursive function to replace previous
# value 'prevV' at '(x, y)' and all surrounding
# values of (x, y) with new value 'newV'.
def floodFillUtil(mat, x, y, prevV, newV):
    # Base Cases
    if (x < 0 or x >= M or y < 0 or y >= N):
        return

    if (mat[x][y] != prevV):
        return

    # Replace the color at (x, y)
    mat[x][y] = newV

    # Recur for north, east, south and west
    floodFillUtil(mat, x + 1, y, prevV, newV)
    floodFillUtil(mat, x - 1, y, prevV, newV)
    floodFillUtil(mat, x, y + 1, prevV, newV)
    floodFillUtil(mat, x, y - 1, prevV, newV)


# Returns size of maximum size subsquare
# matrix surrounded by 'X'
def replaceSurrounded(mat):
    # Step 1: Replace all 'O's with '-'
    global M, N
    M = len(mat)
    N = len(mat[0])
    for i in range(M):
        for j in range(N):
            if (mat[i][j] == 'O'):
                mat[i][j] = '-'

    # Call floodFill for all '-'
    # lying on edges
    # Left Side
    for i in range(M):
        if (mat[i][0] == '-'):
            floodFillUtil(mat, i, 0, '-', 'O')

        # Right side
    for i in range(M):
        if (mat[i][N - 1] == '-'):
            floodFillUtil(mat, i, N - 1, '-', 'O')

        # Top side
    for i in range(N):
        if (mat[0][i] == '-'):
            floodFillUtil(mat, 0, i, '-', 'O')

        # Bottom side
    for i in range(N):
        if (mat[M - 1][i] == '-'):
            floodFillUtil(mat, M - 1, i, '-', 'O')

        # Step 3: Replace all '-' with 'X'
    for i in range(M):
        for j in range(N):
            if (mat[i][j] == '-'):
                mat[i][j] = 'X'
    return mat

# Driver code
if __name__ == '__main__':

    mat = [['X', 'O', 'X', 'O', 'X', 'X'],
           ['X', 'O', 'X', 'X', 'O', 'X'],
           ['X', 'X', 'X', 'O', 'X', 'X'],
           ['O', 'X', 'X', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'O', 'X', 'O'],
           ['O', 'O', 'X', 'O', 'O', 'O']];

    replaceSurrounded(mat)

    for i in range(M):
        print(*mat[i])

    # This code is contributed by himanshu77
