def maxHeight(wallPositions, wallHeights):
    n = len(wallPositions)
    maxheight = 0
    for i in range(n-1):
        heightDiff  = abs(wallHeights[i + 1] - wallHeights[i])
        gapLen = wallPositions[i + 1] - wallPositions[i] - 1
        if gapLen > heightDiff:
            low = max(wallHeights[i+1], wallHeights[i]) + 1
            remainingGap = gapLen - heightDiff - 1
            localMax = low + remainingGap // 2
        else:
            localMax = min(wallHeights[i + 1], wallHeights[i]) + gapLen
        maxheight = max(maxheight, localMax)

    return maxheight
print(maxHeight([1, 10],  [1, 5]))