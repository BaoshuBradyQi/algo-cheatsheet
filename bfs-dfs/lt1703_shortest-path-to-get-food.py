"""
bfs solution
keep tracking boundary,
if food in boundary return the number of iterations
if boundary is empty, return -1
mark visited path with 'wall'
time complexity: O(mn)
space complexity: O(m + n), depends on the scale of m and n
"""
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        start = set()
        for r_idx in range(0, len(grid)):
            for c_idx in range(0, len(grid[r_idx])):
                if grid[r_idx][c_idx] == '*':
                    start.add((r_idx, c_idx))
                    break
        ret = 0
        while start:
            boundary = set()
            ret += 1
            for p in start:
                r_idx, c_idx = p
                grid[r_idx][c_idx] = "X"
                if r_idx - 1 >= 0: # up
                    if grid[r_idx - 1][c_idx] == "O":
                        boundary.add((r_idx -1, c_idx))
                    elif grid[r_idx - 1][c_idx] == "#":
                        return ret
                if r_idx + 1 < len(grid): # down
                    if grid[r_idx + 1][c_idx] == "O":
                        boundary.add((r_idx +1, c_idx))
                    elif grid[r_idx + 1][c_idx] == "#":
                        return ret
                if c_idx - 1 >= 0: # left
                    if grid[r_idx][c_idx - 1] == "O":
                        boundary.add((r_idx, c_idx - 1))
                    elif grid[r_idx][c_idx - 1] == "#":
                        return ret
                if c_idx + 1 < len(grid[0]): # right
                    if grid[r_idx][c_idx + 1] == "O":
                        boundary.add((r_idx, c_idx + 1))
                    elif grid[r_idx][c_idx + 1] == "#":
                        return ret
            start = boundary.copy()
        return -1



