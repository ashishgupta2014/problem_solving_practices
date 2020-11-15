s = 'abc'
set = set()
def solve(input, output=[]):
    """
    print all possible sequence subsets of string
    power sequence subset is also same as all sequence subset
    :param input:
    :param output:
    :return:
    """
    if len(input) == 0:
        print(''.join(output))
        set.add(''.join(output))
        return
    op1 = output.copy()
    op2 = output.copy()
    op2.append(input[0])
    input = input[1:]
    solve(input, op1)
    solve(input, op2)
solve(s)
print(set)