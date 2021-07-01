"""
simple dfs solutions, starting from the edge of grid, mark land as water
then loop through all cells in grid, count the island

Time complexity: O(m * n)
Space complexity: O(1)
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        n_row = len(grid)
        n_col = len(grid[0])
        moves = [0, 1, 0, -1, 0]
        def dfs(r_idx, c_idx):
            if grid[r_idx][c_idx] == 1:
                return
            grid[r_idx][c_idx] = 1
            for idx in range(4):
                new_r, new_c = r_idx + moves[idx], c_idx + moves[idx + 1]
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 0:
                    dfs(new_r, new_c)

        for r_idx in range(n_row):
            dfs(r_idx, 0)
            dfs(r_idx, n_col - 1)
        for c_idx in range(n_col):
            dfs(0, c_idx)
            dfs(n_row - 1, c_idx)

        for r_idx in range(n_row):
            for c_idx in range(n_col):
                if grid[r_idx][c_idx] == 0:
                    ret += 1
                    dfs(r_idx, c_idx)
        return ret
