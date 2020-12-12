def fill_water(water, glasses, row, column):
    """
    https://app.glider.ai/practice/problem/algorithms/water-fill-glasses/problem

    There is a stack of water glasses in a form of pascal triangle and a person wants to pour the water only at the
    topmost glass, but the capacity of each glass is 1 unit . Overflow takes place in such a way that after 1 unit, 1/2
    of remaining unit gets into immediate below left glass and other half in immediate below right glass.
                            1
                       /        \
                    2             3
                /      \       /      \
           4              5              6
    Now the person pours K units of water in the topmost glass and wants to know how much water is there in the jth glass of the ith row.
    Assume that there are enough glasses in the triangle till no glass overflows.

    Input
    First line contain an integer K, second line contains an integer i and third line contains an integer j.

    Output
    Corresponding to each test case output the remaining amount of water in jth cup of the ith row correct to 6 decimal places.

    :param water:
    :param glasses:
    :param row:
    :param column:
    :return:
    """
    if glasses[row][column] + water <= 1:  # no overflow, so we terminate the loop
        glasses[row][column] += water
        return
    extra_water = glasses[row][column] + water - 1
    glasses[row][column] = 1 # fill the glass
    fill_water(extra_water/2, glasses, row + 1, column)  # divide the water into two glasses
    fill_water(extra_water/2, glasses, row + 1, column + 1)

k = 4
n = 2-1
glasses = [[0] * (i + 1) for i in range(k)]
print(glasses)
position = 2 - 1

fill_water(k, glasses, 0, 0)
print(glasses)
print(glasses[n][position])