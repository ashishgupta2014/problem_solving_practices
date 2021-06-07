"""
https://app.codesignal.com/challenge/24P5HwcFMk9MCfLyY?solutionId=QYMToZTaSQyoFqZXm

Once upon a time, in a kingdom far, far away, there lived a King Byteasar V. His predecessor, King Byteasar IV, lived quite a long life, and when Byteasar V finally ascended to the throne, he was already 150 years old. The new king had been preparing all his life for his moment of glory and, scared that he wouldn't have enough time to shine, started his reforms right away. The first (and, as it turned out, the last) royal decree, issued within a couple of days of the coronation, ordered the following: each and every road in the kingdom was to be named.

Unfortunately the king didn't have enough time to come up with actual names, so all the roads were to be names with numbers from 0 to roads.length - 1. As a born strategist, Byteasar wanted to make sure that the maps of his kingdom were confusing to enemies, which is why the road names were to be chosen so that no two roads with neighboring names would have a common end.

The official cartographers came up with names for the roads, but they're not sure if the constraint the king imposed was actually met, and it's your job to help them out. Given the names for the roads the cartographers came up with, check that no two roads with neighboring names have a common end.

Example

For

roads = [[0, 1, 0],
         [4, 1, 2],
         [4, 3, 4],
         [2, 3, 1],
         [2, 0, 3]]
the output should be
namingRoads(roads) = true.

Here's what the given road system looks like:



For

roads = [[2, 3, 1],
         [3, 0, 0],
         [2, 0, 2]]
the output should be
namingRoads(roads) = false.

Here's what the given road system looks like:



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer roads

Array of two-way roads with their names. Each road is given in the format [city1, city2, road_name], where city1 ≠ city2, and 0 ≤ road_name < roads.length. It is guaranteed that there are no duplicate roads or roads with the same name.

Guaranteed constraints:
1 ≤ roads.length ≤ 35000,
roads[i].length = 3,
roads[i][0] ≠ roads[i][1],
0 ≤ roads[i][2] < roads.length,
0 ≤ roads[i][j] ≤ 35000,
roads[i][2] ≠ roads[j][2], i ≠ j.

[output] boolean

true if the names of the roads will be confusing to enemies, false otherwise.
"""





def namingRoads(r):
    r.sort(key = lambda x: x[2])
    for i in range(len(r) - 1):
        for e in r[i][:2]:
            if e in r[i + 1][:2]:
                return False
    return True
roads = [[0, 1, 0],
         [4, 1, 2],
         [4, 3, 4],
         [2, 3, 1],
         [2, 0, 3]]
print(namingRoads(roads))