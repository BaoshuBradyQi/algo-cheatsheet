"""
bfs
time complexity: O(n^2)
space complexity: O(n)

"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return 1
        length = 1
        boundary =  {(0, 0)}
        while boundary:
            length += 1
            new_boundary = set()
            for p in boundary:
                next_step = {
                    (p[0] - 1, p[1]), # up
                    (p[0], p[1] - 1), # left
                    (p[0] + 1, p[1]), # down
                    (p[0], p[1] + 1), # right
                    (p[0] + 1, p[1] + 1), # dia
                    (p[0] - 1, p[1] - 1), #
                    (p[0] + 1, p[1] - 1), #
                    (p[0] - 1, p[1] + 1), #

                }
                valid = list(filter(lambda x: 0 <= x[0]  and x[0] < len(grid) and 0 <= x[1] and x[1] < len(grid) and grid[x[0]][x[1]] == 0 and (x), next_step))
                if (len(grid) -1, len(grid) - 1) in valid:
                    return length
                new_boundary.update(valid)
                grid[p[0]][p[1]] =1
            if not new_boundary:
                return -1
            boundary = new_boundary
        return -1