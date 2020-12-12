"""
Bit Manipulation  Notes

https://www.geeksforgeeks.org/python-bitwise-operators/

first convert number to binary then perform operations

>> left shift ==> number1 >> number2 ==> number1 * power(2, number2) ==>add zeros at left side
<< right shift ==> number1 << number2 ==> number1//power(2, number2) ==>add zeros at right side

& and operation ==> 0 & 0 = 0, 0 & 1 = 0, 1 & 0 = 0, 1 & 1 = 1
| or operation ==> 0 | 0 = 0, 0 | 1 = 1, 1 | 0 = 0, 1 | 1 = 1
^ xor operation ==> 0 ^ 0 = 1, 0 ^ 1 = 1, 1 ^ 0 = 0, 1 ^ 1 = 1
~ not operation ==> ~0 = 1, ~1 = 0

"""



def countBits(a, b):
    """
    https://www.geeksforgeeks.org/count-number-of-bits-to-be-flipped-to-convert-a-to-b-set-2/

    https://app.glider.ai/tutorials/count-number-of-bits-that-need-to-flip-to-convert-/problem

    You are given two numbers A and B. Write a program to count number of bits needed to be flipped to convert A to B.

    Input
    The first line of each test case are two space seperated numbers.

    Output
    Print the number of bits needed to be flipped.

    Constraints
    1 ≤ A,B ≤ 1000

    :param a:
    :param b:
    :return:
    """
    # To store the required count
    count = 0

    # Loop until both of them become zero
    while (a or b):

        # Store the last bits in a
        # as well as b
        last_bit_a = a & 1
        last_bit_b = b & 1

        # If the current bit is not same
        # in both the integers
        if (last_bit_a != last_bit_b):
            count += 1

        # Right shift both the integers by 1
        a = a >> 1
        b = b >> 1

    # Return the count
    return count


# Driver code
a = 10
b = 7

print(countBits(a, b))