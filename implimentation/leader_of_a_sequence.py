from itertools import permutations
def sequence_leader(number):
    """
    https://app.glider.ai/practice/problem/basic-programming/the-leader-of-a-sequence/problem

    A sequence of integers can be formed using integers from 0 to n (inclusive). These numbers want to choose their
    leader, which is a number itself (not necessarily from this sequence). The leader of the sequence
    a0 , a1, a2, ..., an​ is the following number: "Leader" = (0 xor a0) + (1 xor a1) + ... + (n xor an).
    You are given an integer n. You must generate the sequence of integers (using 0, 1, ..., n) such that
    their leader should be maximal.

    alternate solution for better performance
    return (number + 1) * number

    :param number:
    :return:
    """
    m = 0
    for p in list(permutations(range(0, number+1))):
        s = 0
        for index, val in enumerate(p):
            s += index ^ val
        m = max(s, m)
    return m
print(sequence_leader(1))