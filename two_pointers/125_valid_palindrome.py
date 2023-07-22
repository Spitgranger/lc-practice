# Valid palindrome, two pointers, one starting at start of phrase, one at end
# if the characters at the two pointers are equal, increment the counter, if not return false
# repeat until the pointers cross each other

def valid_palindrome(s):
    removedSpecial = ''.join(char for char in s if char.isalnum()).lower()
    start = 0 
    end = len(removedSpecial) - 1
    while start <= end:
        if removedSpecial[start] != removedSpecial[end]:
            return False
        else:
            start += 1
            end -= 1
    return True