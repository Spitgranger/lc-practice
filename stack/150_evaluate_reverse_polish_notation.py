# The idea is this: iterate through the tokens if it is not a operator, push it onto the stack if operator,
# pop the previous two items off the stack and evaluate it and push it back onto the stack. Repeat until reaching
# the end of tokens, then the result should be the only element in the stack so return stack.pop(). This takes O(n) time
def evalRPN(tokens) -> int:
    stack = []
    for token in tokens:
        if token in "+-*/" and token:
            b = int(stack.pop())
            a = int(stack.pop())
            if token == "+":
                stack.append(str(a+b))
            elif token == "-":
                stack.append(str(a-b))
            elif token == "*":
                stack.append(str(a*b))
            elif token == "/":
                stack.append(str(int(a/b)))
        else:
            stack.append(token)
    return int(stack.pop())