def search(arr, key):
    """
    https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/
    SEARCH IN A ROW WISE AND COLUMN WISE SORTED MATRIX:

    Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. Otherwise,
     print “Not Found”. In the given matrix, every row and column is sorted in increasing order.
     The designed algorithm should have linear time complexity.
    :param arr:
    :param key:
    :return:
    """
    row = len(arr)
    col = len(arr[0])
    i = 0
    j = col - 1
    while True:
        if (0 > j < col) or (0 > i < row):
            return -1
        if arr[i][j] == key:
            return i, j
        elif arr[i][j] > key:
            j -= 1
        else:
            i += 1
            
arr =  [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
key = 50
print(search(arr, key))


