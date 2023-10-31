from typing import List
def maxAreaOfIsland(grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        # def dfs(x, y):
        #     if x < 0 or y < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 0:
        #         visited.add((x, y))
        #         return 0
        #     visited.add((x, y))
        #     return 1 + dfs(i, j - 1) + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j + 1)

        # The idea is to run a dfs at each position on the grid on the island. Keeping track of the current max area and every time a recursive call is made,
        # and the current position is 1, return 1 + the dfs of all surrounding neighbours. This will eventually return the max area of the island.
        def dfs(i, j, current_area):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 0:
                return 0    
            visited.add((i,j))
            return (1 + dfs(i, j - 1, current_area + 1) + dfs(i - 1, j, current_area + 1)
            + dfs(i + 1, j, current_area + 1)
            + dfs(i, j + 1, current_area + 1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the current position is not 0, there is a chance that this is the new max area
                if grid[i][j] != 0:
                    max_area = max(max_area, dfs(i, j, 0))
        return max_area

print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])) 