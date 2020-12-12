def maxHeight(wallPositions, wallHeights):
    """
    https://leetcode.com/discuss/interview-question/885181/smartlinks-oa-dam-design

    https://fizzbuzzer.com/mud-walls/

    A child likes to build mud walls by placing mud between sticks positioned on a number line. The gap between sticks
    will be referred to as a cell, and each cell will contain one segment of wall. The height of mud in a segment
    cannot exceed 1 unit above an adjacent stick or mud segment. Given the placement of a number of sticks and their
    heights, determine the maximum height segment of mud that can be built. If no mud segment can be built, return 0.


    For example, there are n = 3 sticks at stickPositions = [1, 2, 4, 7] with stickHeights = [4, 5, 7, 11]. There is no
    space between the first two sticks, so there is no cell for mud. Between positions 2 and 4, there is one cell.
    Heights of the surrounding sticks are 5 and 7, so the maximum height of mud is 5 + 1 = 6. Between positions 4 and 7
    there are two cells. The heights of surrounding sticks are 7 and 11. The maximum height mud segment next to the
    stick of height 7 is 8. The maximum height mud next to a mud segment of height 8 and a stick of height 11 is 9.
    Mud segment heights are 6, 8 and 9, and the maximum height is 9. In the table below, digits are in the columns of
    sticks and M is in the mud segments.

    :param wallPositions:
    :param wallHeights:
    :return:
    """
    n = len(wallPositions)
    if n != len(wallHeights):
        return 0
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
        if gapLen:
            maxheight = max(maxheight, localMax)

    return maxheight
print(maxHeight([4, 5, 6, 9, 10, 11, 12, 13, 14],  [20, 22, 11, 14, 14, 21, 19, 14, 23]))