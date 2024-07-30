# The solution is to break the string down into smaller problems. Its important to realize that the inner strings must be decoded first before the outer ones.
# The algorithm is as follows, maintain a stack. For each character in the string add it to the stack if its not "]", else pop until we hit "[" storing the popped elements
# in a temporary variable. Then, keep poping as long as the character is a number. At the end, add to the stack the number times the temporary variable. and at the end return the joined string.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                temp = []
                while True:
                    element = stack.pop()
                    if element == "[":
                        break
                    temp.append(element)
                num = []
                while True:
                    if not stack or not stack[-1].isnumeric():
                        break
                    num.append(stack.pop())
                for _ in range(int("".join(reversed(num)))):
                    stack.append("".join(reversed(temp)))
        return "".join(stack)
