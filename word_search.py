dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = 'ABCCED'


def exist():
    ## RC ##
    ## RECURSIVE ##
    ## similar to Number of Islands ##
    def search(board, i, j, word):

        if (len(word) == 0):
            return True

        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]):
            return False

        temp = board[i][j]
        board[i][j] = '$'

        result = search(board, i + 1, j, word[1:]) or search(board, i - 1, j, word[1:]) or search(board, i, j + 1,
                                                                                                  word[1:]) or search(
            board, i, j - 1, word[1:])

        board[i][j] = temp
        return result

    for i in range(len(board)):
        for j in range(len(board[0])):
            if search(board, i, j, word):
                return True
    return False
print(exist())