from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def visit_cell(i, j):
            if (i,j) in visited:
                return 0
            if i < 0 or j < 0:
                return 0
            if i >= rows or j >= cols:
                return 0
            if grid[i][j] != "1":
                return 0
            
            visited.add((i,j))
            for di, dj in drs:
                visit_cell(i + di, j + dj)
            return 1

        for i in range(rows):
            for j in range(cols):
                count += visit_cell(i ,j)

        return count