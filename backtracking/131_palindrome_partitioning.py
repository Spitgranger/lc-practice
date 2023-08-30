from typing import List
def partition(s: str) -> List[List[str]]:
    output = []
    cur = []
    def isPalindrome(string):
        i = 0
        j = len(string) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def dfs(current):
        if current >= len(s):
            output.append(cur.copy())
            return
        for i in range(current, len(s)):
            print(s[current:i+1], isPalindrome(s[current:i+1]))
            if isPalindrome(s[current:i+1]):
                cur.append(s[current:i+1])
                dfs(i+1)
                cur.pop()
    dfs(0)
    return output
def isPalindrome(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    print(isPalindrome("ab"))