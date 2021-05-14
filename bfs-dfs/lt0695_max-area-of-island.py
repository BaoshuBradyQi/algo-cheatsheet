"""
dfs solution, set visited land to water and use dfs to track how many times we set 1 to water

time complexity: O(n * m)
space complexity: O(1), no extra space
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        n_row = len(grid)
        n_col = len(grid[0])

        maxarea = 0
        def dfs(r_idx, c_idx):
            ret = 0
            grid[r_idx][c_idx] = 0
            if r_idx + 1 < n_row and grid[r_idx + 1][c_idx] == 1:
                grid[r_idx+1][c_idx] = 0
                ret += dfs(r_idx + 1, c_idx) + 1
            if r_idx - 1 >=0 and grid[r_idx -1][c_idx] == 1:
                grid[r_idx - 1][c_idx] = 0
                ret += dfs(r_idx - 1, c_idx) + 1
            if c_idx +1 < n_col and grid[r_idx][c_idx + 1] == 1:
                grid[r_idx ][c_idx + 1] = 0
                ret += dfs(r_idx, c_idx  + 1) + 1
            if c_idx - 1 >= 0 and grid[r_idx][c_idx - 1] ==1:
                grid[r_idx][c_idx - 1] = 0
                ret += dfs(r_idx, c_idx - 1) + 1
            return ret

        for r_idx in range(0, n_row):
            for c_idx in range(0, n_col):
                if grid[r_idx][c_idx] == 1:
                    maxarea = max(maxarea, 1 + dfs(r_idx, c_idx))


        return maxarea
