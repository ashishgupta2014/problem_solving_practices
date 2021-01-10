"""
https://app.glider.ai/practice/problem/algorithms/paint/problem

In Paint, when we take a Shape Filler and click on a pixel, the color of the region is replaced with a selected color.
For a given screen as a 2D array (size of N x M) of colored pixels, S{X, Y} pixel and new color C, replace the color of
the given pixel and all adjacent same-colored pixels with color C.

Input
The first line of input contains an integer N, representing the number of rows.
The second line of input contains an integer M, representing the number of columns.
The next N lines of input contain M space-separated integers, representing row elements as pixel colors.
The next 3 lines of input contain integers X, Y, C, representing the pixel index points S(X, Y) and new color.​​​

Output
Print the updated 2D matrix as a screen.

Constraints
1 <= N, M <= 100
0 <= X,Y <= 100
0 <= C <= 1000

"""



def search_by_direction(ar, row, col, direction, num, replace_num):
    """

    :param ar:
    :param row:
    :param col:
    :param direction:
    :param num:
    :param replace_num
    :return:
    """
    if row >= len(ar) or col >= len(ar[0]) or row <= -1 or col <= -1 or ar[row][col] != num:
        return
    ar[row][col] = replace_num
    for i, j in direction:
        search_by_direction(ar, row+i, col+j, direction, num, replace_num)


def color(ar, X, Y, C):
    """

    :param ar:
    :param X:
    :param Y:
    :param C:
    :return:
    """
    row = len(ar) - 1
    col = len(ar[0]) - 1
    direction = [(-1, -1),  (-1, 0),  (-1, 1),  (0, -1),  (0, 1),  (1, -1),  (1, 0),  (1, 1)]
    search_by_direction(ar, row, col, direction, ar[X][Y], C)
a = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 1, 1, 0],[0, 1, 1, 1, 1],[0, 0, 0, 1, 1]]
color(a, 2, 2, 3)
print(a)
