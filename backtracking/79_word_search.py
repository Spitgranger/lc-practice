def exist(board, word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(i, j, index):
            if len(word) == index:
                return True
            if i >= rows or j >= cols or rows < 0 or cols < 0 or board[i][j] != word[index] or (i, j) in visited:
                return False
            visited.add((i,j))
            res = dfs(i + 1, j, index + 1) or dfs(i, j + 1, index + 1) or dfs(i - 1, j, index + 1) or dfs(i, j - 1, index + 1)
            visited.remove((i, j))
            return res

        for a in range(rows):
            for b in range(cols):
                if dfs(a, b, 0):
                    return True
        return False


if __name__ == '__main__':
    board = [["a", "a"]]
    word = "aaa"
    print(exist(board, word))
