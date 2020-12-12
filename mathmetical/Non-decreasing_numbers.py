def countNonDecreasing(n):
    """
    https://app.glider.ai/practice/problem/algorithms/nondecreasing-numbers/problem

   https://www.geeksforgeeks.org/total-number-of-non-decreasing-numbers-with-n-digits/

    You have given with a count of digits N. Print the count of total non-decreasing numbers having N digits.
    A number is non-decreasing if every digit (except the first one) is greater than or equal to the previous digit.

    Input
    The input contains an integer N.

    Output
    Print the count of total non-decreasing numbers having N digits.

    Constraints
    1 <= N <= 30


    :param n:
    :return:
    """
    N = 10

    # Compute value of N*(N+1)/2*(N+2)/3
    # * ....*(N+n-1)/n
    count = 1
    for i in range(1, n + 1):
        count = int(count * (N + i - 1))
        count = int(count / i)

    return count


# Driver program
n = 3
print(countNonDecreasing(n))