"""
https://app.glider.ai/practice/problem/algorithms/circular-array/problem

https://www.geeksforgeeks.org/maximize-sum-consecutive-differences-circular-array/

For a given circular array a[](element after an is a1), find the maximum possible sum of the differences between consecutive elements with rearrangement of array element allowed i.e after rearrangement of element find  |a1 – a2| + |a2 – a3| + …… + |an – 1 – an| + |an – a1|, which results maximum sum.

Input
The first line of input contains an integer N, denotes the size of the array.
The second line of input contains N space-separated integers, denoting the array elements.

Output
The maximum sum of the differences.

Constraints
1 <= N <= 10000

Example #1
Input
4
2 4 1 8
Output
18
Explanation: We can rearrange given array as 1, 8, 2, 4 which reults maximum sum.
sum of neighbor elements will be :
|1 - 8| + |8 - 2| + |2 - 4| + |4 - 1| = 18
Example #2
Input
3
10 12 15
Output
10
Explanation: |10 - 12| + |12 - 15| + |15 - 10| = 10

"""

def maxSum(arr, n):
    sum = 0

    # Sorting the array
    arr.sort()

    # Subtracting a1, a2, a3,....., a(n/2)-1, an/2
    # twice and adding a(n/2)+1, a(n/2)+2, a(n/2)+3,.
    # ...., an - 1, an twice.
    for i in range(0, n // 2):
        sum -= (2 * arr[i])
        sum += (2 * arr[n - i - 1])

    return sum


# Driver Program
arr = [4, 2, 1, 8]
n = len(arr)
print(maxSum(arr, n))