"""
bfs solution, water is starting points, then do bfs to extend to land

time complexity: O(m * n)
space complexity: O(m * n)
possible improvement, do in-place update, so no extra space needed
"""
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix and not matrix[0]:
            return matrix

        n_row = len(matrix)
        n_col = len(matrix[0])

        ret = [[-1 for i in range(0, n_col)] for j in range(0, n_row)]

        cur = set()
        for r_idx, row in enumerate(matrix):
            for c_idx, col in enumerate(row):
                if col ==0:
                    cur.add((r_idx, c_idx))

        level = 0
        while cur:
            for r_idx, c_idx in cur:
                ret[r_idx][c_idx] = level

            level += 1
            new_cur = set()
            for r_idx, c_idx in cur:
                if r_idx - 1 >= 0 and ret[r_idx - 1][c_idx] == -1:
                    new_cur.add((r_idx - 1, c_idx))
                if r_idx + 1 < n_row and ret[r_idx + 1][c_idx] == -1:
                    new_cur.add((r_idx + 1, c_idx))
                if c_idx - 1 >= 0 and ret[r_idx][c_idx - 1] == -1:
                    new_cur.add((r_idx, c_idx - 1))
                if c_idx + 1 < n_col and ret[r_idx][c_idx + 1] == -1:
                    new_cur.add((r_idx, c_idx+1))

            cur = new_cur
        return ret
