"""
dp solution, counting the dimension of squares with all ones in place
square with all ones should be the minimal in width, height, and diagonal

Time complexity: O(m * n)
Space complexity: O(# of rows), due to the sum function, but can do it in constant space
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ret = 0
        if not matrix or not matrix[0]:
            return ret
        for r_idx, row in enumerate(matrix):
            for c_idx, col in enumerate(row):
                if col and r_idx > 0 and c_idx > 0 :
                    matrix[r_idx][c_idx] = min(matrix[r_idx - 1][c_idx], matrix[r_idx - 1][c_idx - 1], matrix[r_idx][c_idx - 1]) + 1
        return sum([sum(row) for row in matrix])
