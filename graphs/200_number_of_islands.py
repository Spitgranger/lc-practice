from typing import List
# This is a O(n * m) solution. The idea is exactly the same as finding all connected components in a graph.
# Run dfs on every number that is not 0. If we haven't visited it, increment the number of islands by one.
def numIslands(grid: List[List[str]]) -> int:
    visited = set()
    number = 0
    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or (i, j) in visited or grid[i][j] == '0':
            return
        visited.add((i, j))
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == '1':
                number += 1
            dfs(i, j)
    return number

#SOlution without set keeping track of visited nodes, set each element of grid to '0' after visiting them
def numIslands(grid: List[List[str]]) -> int:
    number = 0
    height = len(grid)
    width = len(grid[0])
    def dfs(i, j):
        if i >= height or j >= width or i < 0 or j < 0 or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                number += 1
            dfs(i, j)
    return number
