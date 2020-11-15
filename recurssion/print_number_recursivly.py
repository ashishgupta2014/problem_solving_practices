def print_1_to_n(n):
    """

    :param n:
    :return:
    """
    if n == 1:
        print(n)
        return
    print_1_to_n(n-1)
    print(n)
print_1_to_n(10)

print('------------------------')
def print_n_to_1(n):
    """

    :param n:
    :return:
    """
    if n == 1:
        print(n)
        return
    print(n)
    print_n_to_1(n-1)
print_n_to_1(10)

print('-----Factorial---------')
def factorial(n):
    """

    :param n:
    :return:
    """
    if n == 1:
        return 1
    ans = 1
    ans *= n*factorial(n-1)
    return ans
print(factorial(5))