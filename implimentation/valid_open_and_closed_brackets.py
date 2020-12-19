def solve(string):
    """

    :param string:
    :return:
    """
    count = 0
    for i in range(len(string)):
        if count and string[i] == ')':
            count -= 1
        else:
            count += 1

    if not count:
        print('Valid')
    else:
        print('Invalid')
solve('(()))(')