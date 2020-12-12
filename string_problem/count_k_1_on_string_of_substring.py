def solve(K,s):
    """
    https://app.glider.ai/practice/problem/algorithms/exactly-k-1s/problem

    https://www.geeksforgeeks.org/count-substrings-binary-string-containing-k-ones/


    You are given a binary string  i.e, a string that contains only 1s and 0s.
    You must count the number of sub strings which contain exactly K 1s.
    :param K:
    :param s:
    :return:
    """
    N = len(s)
    res = 0
    countOfOne = 0
    freq = [0 for _ in range(N + 1)]

    # initialize index having
    # zero sum as 1
    freq[0] = 1

    # loop over binary characters of string
    for i in s:

        # update countOfOne variable with
        # value of ith character
        countOfOne += ord(i) - ord('0')

        # if value reaches more than K,
        # then update result
        if (countOfOne >= K):
            # add frequency of indices, having
            # sum (current sum - K), to the result
            res += freq[countOfOne - K]

            # update freqency of one's count
        freq[countOfOne] += 1

    return res

if __name__ == '__main__':
    k = 3
    s = '00101010'

    outcome = solve(k, s)

    print(outcome)