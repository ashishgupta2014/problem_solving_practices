from collections import Counter
from functools import lru_cache

d = Counter('i like sam sung samsung mobile ice cream icecream man go mango a animal'.split())

string = 'ianimal'
n = len(string)

@lru_cache(maxsize=None)
def work_break(string):
    """

    :param string:
    :return:
    """
    n = len(string)
    if n == 0:
        return True
    for i in range(n):
        if string[:i+1] in d and work_break(string[i+1:n]):
            return True
    else:
        return False


print(work_break(string))