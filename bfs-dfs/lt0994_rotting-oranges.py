"""
bfs solution, rotten ones are starting points, then do bfs

time complexity: O(n * m )
space complexity: O(# of boundaries)

"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r_num = len(grid)
        c_num = len(grid[0])

        cur = set()
        oranges = 0
        for r_idx, row in enumerate(grid):
            for c_idx, col in enumerate(row):
                if col == 2:
                    cur.add((r_idx, c_idx))
                elif col == 1:
                    oranges += 1
        ret = 0
        rotten = 0

        while cur:
            new_cur = set()

            for r_idx, c_idx in cur:
                if r_idx - 1 >= 0 and grid[r_idx - 1][c_idx] == 1:
                    new_cur.add((r_idx - 1, c_idx))

                if r_idx + 1 < r_num and grid[r_idx + 1][c_idx] == 1:
                    new_cur.add((r_idx + 1, c_idx))
                if c_idx - 1 >= 0 and grid[r_idx ][c_idx - 1] == 1:
                    new_cur.add((r_idx, c_idx -1))
                if c_idx + 1 < c_num and grid[r_idx][c_idx + 1] == 1:
                    new_cur.add((r_idx, c_idx + 1))
            for r_idx, c_idx in new_cur:
                grid[r_idx][c_idx] = 2
            rotten += len(new_cur)
            cur = new_cur
            if new_cur:
                ret += 1

        return ret if rotten == oranges else -1
