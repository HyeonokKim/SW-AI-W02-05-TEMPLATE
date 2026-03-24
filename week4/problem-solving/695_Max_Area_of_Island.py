# Leetcode 695
# DFS/BFS

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        result = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0 
            
            grid[r][c] = 0

            area = 1
            area += dfs(r-1,c)
            area += dfs(r+1,c)
            area += dfs(r, c-1)
            area += dfs(r, c+1)

            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    result = max(result, dfs(i,j))

        return result