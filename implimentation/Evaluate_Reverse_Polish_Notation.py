import math

op = {'-', '+', '*', '/'}
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in op:
            stack.append(int(token))
        else:
            sec_operand = stack.pop()
            fir_operand = stack.pop()
            tmp = 0
            if token == '+':
                tmp = fir_operand + sec_operand
            elif token == '-':
                tmp = fir_operand - sec_operand
            elif token == '*':
                tmp = fir_operand * sec_operand
            elif token == '/':
                tmp = math.trunc(fir_operand / sec_operand)
            stack.append(tmp)
    return stack.pop()
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))