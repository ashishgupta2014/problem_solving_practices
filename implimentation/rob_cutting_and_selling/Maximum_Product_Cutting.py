"""
https://www.geeksforgeeks.org/maximum-product-cutting-dp-36/

Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of
lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters.
Examples:

Input: n = 2
Output: 1 (Maximum obtainable product is 1*1)

Input: n = 3
Output: 2 (Maximum obtainable product is 1*2)

Input: n = 4
Output: 4 (Maximum obtainable product is 2*2)

Input: n = 5
Output: 6 (Maximum obtainable product is 2*3)

Input: n = 10
Output: 36 (Maximum obtainable product is 3*3*4)
"""
def maxProd(n):
    # n equals to 2 or 3 must
    # be handled explicitly
    if n == 2 or n == 3:
        return n - 1

    # Keep removing parts of size 3
    # while n is greater than 4
    res = 1
    while n > 4:
        n -= 3

        # Keep multiplying 3 to res
        res *= 3

    # The last part multiplied
    # by previous parts
    return n * res


# Driver program to test above functions
print("Maximum Product is ", maxProd(10));