

def CheckLuckyNumber(number):
    """
    https://app.glider.ai/practice/problem/basic-programming/lucky-numbers/problem


    John found another manuscript of ancient mathematicians. According to this manuscript an integer k is a
    lucky number if k = a1​​​​ + a​​​2​​​ + ... + ​a​​​n​​​​,
    where​​​:
    ai = 7p. p may be any positive integer.
    if i and j are distinct, ai != aj
    :param number:
    :return:
    """
    if number < 7:
        return 0

    i = 1
    temp = 7
    while pow(7, i) <= number:
        i += 1
    if i > 1:
        temp = pow(7, i-1)

    if number == temp:
        return 1


    diff = number - temp
    if diff == temp:
        return 0

    return CheckLuckyNumber(diff)



def solve(array, n):
    count = 0
    for i in range(n):
        count += CheckLuckyNumber(array[i])

    return count

n = 3
array = [56, 49, 50]
print(solve(array, n))
