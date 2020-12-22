def generator(output, string, open, close, n):
    if len(string) == n * 2:
        output.append(string)
        return
    if open < n:
        generator(output, string + '(', open + 1, close, n)
    if close < open:
        generator(output, string + ')', open, close + 1, n)


def generateParenthesis(n):
    output = []
    generator(output, '', 0, 0, n)
    print(output)

generateParenthesis(3)