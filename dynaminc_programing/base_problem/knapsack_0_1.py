"""
https://app.glider.ai/practice/problem/algorithms/01-knapsack-problem/problem

https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60

You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item, In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that Sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0 -1 property).

Input
The first line of input contains an integer N, denotes the number of items and size of array Val[].
The second line of input contains N space-separated positive integers denoting the values of the N items.
The third line of input contains an integer N, denotes the number of items and size of array wt[].
The fourth line of input contains N space-separated positive integers denoting the weights of the N items.
The fifth line of input contains an integer W,  denotes the maximum capacity of the knapsack.

Output
Print the maximum possible value you can get with the given conditions that you can obtain.

Constraints
1≤N≤100
1≤wt[i]≤100
1≤Val[i]≤100
1≤W≤100

Example #1
Input
3
1 2 3
3
4 5 1
4
Output
3
Explantion: Here, Knapsack capacity is 4, possible weight sub set can be [4], [1], sub sets [4], [1] give values
as 1 & 3 respectively, So maximum possible sum is 3 with weight sub set [1].
"""
dp = [[-1 for x in range(11)] for y in range(4)]
def knapsack_recursive(w, v, c, n):
    """
    recursive and memorization technique
    """
    if n == 0 or c == 0:
        return 0
    if dp[n][c] != -1:
        return dp[n][c]
    if w[n-1] <= c:
        dp[n][c] = max((v[n-1] + knapsack_recursive(w, v, c-w[n-1], n-1)), knapsack_recursive(w, v, c, n-1))
    else:
        dp[n][c] = knapsack_recursive(w, v, c, n-1)
    return dp[n][c]
print(knapsack_recursive([2, 5, 7], [60, 100, 120], 10, 3))

def solve_knapsack(profits, weights, capacity):
  """

  :param profits:
  :param weights:
  :param capacity:
  :return:
  """
  n = len(profits)
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0 for x in range(capacity+1)] for y in range(n)]

  # populate the capacity = 0 columns, with '0' capacity we have '0' profit
  for i in range(0, n):
    dp[i][0] = 0

  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(0, capacity+1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  # process all sub-arrays for all the capacities
  for i in range(1, n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
      # exclude the item
      profit2 = dp[i - 1][c]
      # take maximum
      dp[i][c] = max(profit1, profit2)

  # maximum profit will be at the bottom-right corner.
  print(dp)
  return dp[n - 1][capacity]


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()