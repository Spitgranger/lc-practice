# O(2^n) solution
def generateParenthesis(n):
    answer = []
    def dfs(l, r, s):
        if l == 0 and r == 0:
            answer.append(s)
        if l > r:
            return
        if l < r:
            dfs(l, r - 1, s + ")")
        if l > 0:
            dfs(l - 1, r, s + "(")
    dfs(n, n, "")
    return answer