"""
dp solution, if up/left/diagonal are all sqr, that cell should be the min(up, left, diagonal) + 1

time complexity: O(m * n)
space complexity: O(m * n)

improvement, using row instead of entire matrix to store the tmp dp, space complexity would be O(n)
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        r_n = len(matrix)
        c_n = len(matrix[0])

        sqr = [[0 for i in range(0, c_n)] for j in range(0, r_n)]

        for r_idx, _ in enumerate(matrix):
            for c_idx, c in enumerate(matrix[r_idx]):
                if c == "1":
                    if r_idx == 0 or c_idx == 0:
                        sqr[r_idx][c_idx] = 1
                    else:
                        height = sqr[r_idx - 1][c_idx]
                        length = sqr[r_idx][c_idx - 1]
                        diagonal = sqr[r_idx - 1][c_idx - 1]
                        sqr[r_idx][c_idx] = min(height, length, diagonal) + 1
        ret= max([max(r) for r in sqr])
        return ret * ret