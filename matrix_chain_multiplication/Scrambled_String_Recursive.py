a = 'great'
b = 'ategr'


def isScramble(s1, s2):
    """
    https://www.interviewbit.com/problems/scramble-string/
    :param s1:
    :param s2:
    :return:
    """
    if s1 == s2 or s1 == s2[::-1]:
        return True

    for i in range(1, len(s1)):
        if sorted(s1[:i]) == sorted(s2[:i]):
            if isScramble(s1[i:], s2[i:]) and isScramble(s1[:i], s2[:i]):
                return True
        elif sorted(s1[:i]) == sorted(s2[-i:]):
            if isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i]):
                return True
    return False
print(isScramble(a, b))