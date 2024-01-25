import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0


        def dfs(x, y):
            if x not in range(len(grid)) or y not in range(len(grid[0])) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    num_islands += 1
                    dfs(x, y)

        return num_islands


g = [
    ["1", "0", "1", "1", "0", "1", "1"]
]

print(Solution().numIslands(g))
