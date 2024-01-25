import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        def bfs(x, y):
            q = collections.deque()
            q.append((x, y))

            while q:
                x, y = q.popleft()
                if x not in range(len(grid)) or y not in range(len(grid[0])) or grid[x][y] != '1':
                    continue
                grid[x][y] = 0
                q.append((x+1, y))
                q.append((x-1, y))
                q.append((x, y+1))
                q.append((x, y-1))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    num_islands += 1
                    bfs(x, y)

        return num_islands


g = [
    ["1", "0", "1", "1", "0", "1", "1"]
]

print(Solution().numIslands(g))
