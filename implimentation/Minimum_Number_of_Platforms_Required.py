"""
https://app.glider.ai/practice/problem/algorithms/bus-station-problem/problem

https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

Given two arrays, having arrival and departure times of all trains that reach a railway station.
Here, for example, 940 is 09:40, 1120 is 11:20 ...
Find the minimum number of platforms required for the railway station so that no train waits.

Input
The first line of input contains an integer N, denotes the size of an array ar[].
The second line of input contains space-separated N integers as arrival times.
The third line of input contains an integer N, denotes the size of an array de[].
The fourth line of input contains space-separated N integers as departure times.

Output
A minimum number of platforms required for the railway station so that no train waits.

Constraints
1 <= N <= 1000

Example #1
Input
6
900 940 950 1100 1500 1800
6
910 1200 1120 1130 1900 2000
Output
3
Explanation: There are at-most three trains at a time between 11:00 to 11:20.
Example #2
Input
2
1000 1100
2
1200 1300
Output
2
Explanation: There are at-most two trains at a time between 11:00 to 12:00.
"""

def minStation(ar, de):
    """

    :param ar:
    :param de:
    :return:
    """
    n = len(ar)
    ar.sort()
    de.sort()
    i = 1
    j = 0
    plat = 1
    result = 1
    while i < n and j < n:
        if ar[i] <= de[j]:
            plat += 1
            i += 1
        elif ar[i] > de[j]:
            plat -= 1
            j += 1
        if plat > result:
            result = plat

    return result
ar = [900, 940, 950, 1100, 1500, 1800]
de = [910, 1200, 1120, 1130, 1900, 2000]
print(minStation(ar, de))
