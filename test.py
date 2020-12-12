# def maxHeight(wallPositions, wallHeights):
#     n = len(wallPositions)
#     maxheight = 0
#     for i in range(n-1):
#         heightDiff  = abs(wallHeights[i + 1] - wallHeights[i])
#         gapLen = wallPositions[i + 1] - wallPositions[i] - 1
#         if gapLen > heightDiff:
#             low = max(wallHeights[i+1], wallHeights[i]) + 1
#             remainingGap = gapLen - heightDiff - 1
#             localMax = low + remainingGap // 2
#         else:
#             localMax = min(wallHeights[i + 1], wallHeights[i]) + gapLen
#         maxheight = max(maxheight, localMax)
#
#     return maxheight
# #print(maxHeight([1, 10],  [1, 5]))


# def max_list_ele(arr): # [4, 7, 1, 5, 2]
#     n = len(arr)
#     for i in range(n):
#         temp = arr[i+1:]
#         temp.sort()
#         found = -1
#         for j in range(len(temp)):
#             if arr[i] < temp[j]:
# #                 found = temp[j]
# #         arr[i] = found
# # max_list_ele([])


# 0 1 1 2 3 5 ... n

# def fib(n):
#     a = 0
#     b = 1
#     print(a, end=' ') # 0
#     print(b, end=' ') # 1
#     for i in range(1, n):
#         print(a + b, end=' ')
#         a, b = b, i
#
# fib(7)



#   *
#  ***
# *****
#*******


def pattern(n): # 7
    line = n
    i = 1
    space = n - i - 2
    while line > 0:
        print(((' ' * space) + ('*' * i)))
        space -= 2
        i += 2
        line -= 1



pattern(7)




