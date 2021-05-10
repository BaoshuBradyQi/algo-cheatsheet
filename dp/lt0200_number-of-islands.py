"""
dfs solution, mark visited coordinates to 0

time complexity: O(m*n)
space complexity: O(1), using input matrix
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ret = 0
        if not grid:
            return ret
        rows = len(grid)
        cols = len(grid[0])


        def to_water(r_idx, c_idx):
            grid[r_idx][c_idx] = "0"


            if r_idx + 1 < rows and grid[r_idx + 1][c_idx] == "1":
                to_water(r_idx + 1, c_idx)
            if c_idx + 1 < cols and grid[r_idx][c_idx + 1] == "1":
                to_water(r_idx, c_idx + 1)
            if r_idx - 1 >= 0 and grid[r_idx - 1][c_idx] == "1":
                to_water(r_idx - 1, c_idx)
            if c_idx - 1 >= 0 and grid[r_idx][c_idx - 1] == "1":
                to_water(r_idx, c_idx - 1)

        for r_idx, _ in enumerate(grid):
            for c_idx, col in enumerate(grid[r_idx]):
                if col == "1":
                    ret += 1
                    to_water(r_idx, c_idx)
        return ret