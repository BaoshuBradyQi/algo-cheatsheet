"""
not much difference in algorithm comparing to last time,
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = 0
        rotten = set()

        n_row = len(grid)
        n_col = len(grid[0])
        for r_idx in range(n_row):
            for c_idx in range(n_col):
                if grid[r_idx][c_idx] == 2:
                    rotten.add((r_idx, c_idx))
                if grid[r_idx][c_idx] == 1:
                    oranges += 1
        ret = 0
        moves = [0, 1, 0, -1, 0]
        while rotten:
            boundary = set()
            for r_idx, c_idx in rotten:
                for idx in range(4):
                    new_r, new_c = r_idx + moves[idx], c_idx + moves[idx + 1]
                    if 0 <= new_r < n_row and 0 <= new_c < n_col and grid[new_r][new_c] == 1:
                        boundary.add((new_r, new_c))
            for r_idx, c_idx in boundary:
                grid[r_idx][c_idx] = 2
                oranges -= 1
            rotten = boundary
            if rotten:
                ret += 1
        return ret if not oranges else -1
