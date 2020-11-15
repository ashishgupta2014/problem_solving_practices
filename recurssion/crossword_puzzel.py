board = [list('+-++++++++'),
         list('+-++++++++'),
         list('+-------++'),
         list('+-++++++++'),
         list('+-++++++++'),
         list('+------+++'),
         list('+-+++-++++'),
         list('+++++-++++'),
         list('+++++-++++'),
         list('++++++++++')]
words = 'AGRA;NORWAY;ENGLAND;GWALIOR'.split(';')

def canPlaceWordHorizontally(board, word, i, j):
    """

    :param board:
    :param word:
    :param i:
    :param j:
    :return:
    """
    for x in range(len(word)):
        if (j + x) >= 10 or i >= 10:
            return False
        elif board[i][j+x] == '-' or board[i][j+x] == word[x]:
            continue
        else:
            return False
    return True

def placeWordHorizontally(board, word, i, j):
    """

    :param board:
    :param word:
    :param i:
    :param j:
    :return:
    """
    wePlaced = []
    for x in range(len(word)):
        if board[i][x+j] == '-':
            board[i][x+j] = word[x]
            wePlaced.append(True)
        else:
            wePlaced.append(False)
    return wePlaced

def unplaceWordHorizontally(board, wePlaced, i, j):
    """

    :param board:
    :param wePlaced:
    :param i:
    :param j:
    :return:
    """
    for x in range(len(wePlaced)):
        if wePlaced[x]:
            board[i][j+x] = '-'

def canPlaceWordVertically(board, word, i, j):
    """

    :param board:
    :param word:
    :param i:
    :param j:
    :return:
    """
    for x in range(len(word)):
        if (i + x) >= 10 or j >= 10:
            return False
        elif board[i+x][j] == '-' or board[i+x][j] == word[x]:
            continue
        else:
            return False
    return True

def placeWordVertically(board, word, i, j):
    """

    :param board:
    :param word:
    :param i:
    :param j:
    :return:
    """
    wePlaced = []
    for x in range(len(word)):
        if board[i+x][j] == '-':
            board[i+x][j] = word[x]
            wePlaced.append(True)
        else:
            wePlaced.append(False)
    return wePlaced

def unplaceWordVertically(board, wePlaced, i, j):
    """

    :param board:
    :param wePlaced:
    :param i:
    :param j:
    :return:
    """
    for x in range(len(wePlaced)):
        if wePlaced[x]:
            board[i+x][j] = '-'


def solve(board, words, vidx):
    """

    :param board:
    :param words:
    :param vidx:
    :return:
    """
    if vidx == len(words):
        for i in range(10):
            print(board[i])
        return board
    word = words[vidx]
    for i in range(10):
        for j in range(10):
            if board[i][j] == '-' or board[i][j] == word[0]:
                if canPlaceWordHorizontally(board, word, i, j):
                    wePlaced = placeWordHorizontally(board, word, i, j)
                    solve(board, words, vidx + 1)
                    unplaceWordHorizontally(board, wePlaced, i, j)

                if canPlaceWordVertically(board, word, i, j):
                    wePlaced = placeWordVertically(board, word, i, j)
                    solve(board, words, vidx + 1)
                    unplaceWordVertically(board, wePlaced, i, j)

solve(board, words, 0)

