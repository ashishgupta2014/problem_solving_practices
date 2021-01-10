"""
https://app.glider.ai/practice/problem/algorithms/queries-in-array/problem

related problem finding floor and ciel of element in the array using binary search (problem reference ceil_ele_sorted_arr.py)

https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/


Given an array of N integers and Q/2 queries, each includes two integers X and K.
X's are two types:
1. If X is 0, the task is to find the count of elements which are greater than or equal to K
2. If X is 1, the task is to find the count of the elements greater than K

Input
The first line of input contains an integer N, representing the size of the array.
The second line of input contains N space-separated integers, representing the array elements.
The third line of input contains an integer Q, representing the size of the query array.
The fourth line of input contains Q space-separated integers, representing Q/2 pair of integers X and K.

Output
Print the answer to each Query.

Constraints
1 <= N,Q <= 100

Example #1
Input
4
10 20 30 40
8
0 50 1 30 0 30 0 20
Output
0 1 2 3
Explanation:
1. X = 0, K = 50, there are no elements greater than or equal to 50
2. X = 1, K = 30, there is 40 greater than 30
3. X = 0, K = 30, there is 30 and 40, greater than or equal to 30
4. X = 0, K = 20, there is 20, 30 and 40 which are greater than or equal to 20
"""


def binary_search(arr, k):
    """

    :param arr:
    :param k:
    :return:
    """
    l = 0
    h = len(arr) - 1
    res = -1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == k:
            return m
        elif arr[m] < k:
            l = m + 1
        else:
            res = m
            h = m - 1
    return res



def task(ar, q):
    """

    :param ar:
    :param q:
    :return:
    """
    ar.sort()
    result = []
    for i in range(0, len(q), 2):
       if q[i] and q[i+1] > ar[-1]:
           result.append(0)
       else:
           index = binary_search(ar, q[i+1])
           if index != -1:
               if q[i]:
                   result.append(len(ar[index+1:]))
               else:
                   result.append(len(ar[index:]))
           else:
               result.append(0)
    return result
ar = [10, 20, 30, 40]
q = [0, 50, 1, 30, 0, 30, 0, 20]
print(task(ar, q))

