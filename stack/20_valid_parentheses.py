def isValid(s: str) -> bool:
    stack = []
    charmap = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    for char in s:
        if char in "[{(":
            stack.append(char)
        else:
            if stack:
                if charmap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    # Need to check if stack is empty since (){}{ would finish the loop but is invalid
    return not stack