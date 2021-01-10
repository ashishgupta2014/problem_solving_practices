"""
https://app.glider.ai/practice/problem/algorithms/produce-items/problem

https://www.geeksforgeeks.org/minimum-time-required-produce-m-items/

Consider n machines which produce same type of items but at different rate i.e., machine 1 takes a1 sec to produce an
item, machine 2 takes a2 sec to produce an item. Given an array which contains the time required by ith machine to
produce an item. Considering all machine are working simultaneously, the task is to find minimum time required to
produce m items.

Examples:

Input : arr[] = {1, 2, 3}, m = 11
Output : 6
In 6 sec, machine 1 produces 6 items, machine 2 produces 3 items,
and machine 3 produces 2 items. So to produce 11 items minimum
6 sec are required.

Input : arr[] = {5, 6}, m = 11
Output : 30
"""
def minTime(arr, m):
    """

    :param arr:
    :param m:
    :return:
    """
    # Initialise time, items equal to 0.
    t = 0

    while True:

        items = 0

        # Calculating items at each second
        for i in arr:
            items += (t // i)

            # If items equal to m return time.
        if (items >= m):
            return t

        t += 1  # Increment time


# Driver Code
arr = [1, 2, 3]

m = 11

print(minTime(arr, m))

ar = [2, 4, 6]
m = 11
print(minTime(ar, m))