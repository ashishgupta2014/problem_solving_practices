def partiotion(s):
    def isPalindrome(string):
        start = 0;
        end = len(string) - 1
        while (start < end):
            if (string[start] != string[end]):
                return False
            start += 1
            end -= 1
        return True

    def makePartitions(curr, s):

        if (len(s) == 0):
            result.append(curr[:])
            return

        for i in range(1, len(s) + 1):
            if (isPalindrome(s[:i])):
                makePartitions(curr + [s[:i]], s[i:])

    result = []
    makePartitions([], s)
    return result

print(partiotion('aab'))