"""
bottom up dp solution, to get the maximal valid heal point in certain cell

Time complexity: O(mn)
Space complexity: O(1)
"""
class Solution:
    def calculateMinimumHP(self, matrix: List[List[int]]) -> int:

        for r_idx in range(len(matrix) -1, -1, -1):
            for c_idx in range(len(matrix[0] ) -1 , -1, -1):
                if r_idx == len(matrix) - 1 and c_idx == len(matrix[0]) - 1:
                    matrix[r_idx][c_idx] = max(1,  1 - matrix[r_idx][c_idx])
                elif r_idx == len(matrix) - 1:
                    matrix[r_idx][c_idx] = max(1, matrix[r_idx][c_idx + 1] - matrix[r_idx][c_idx])
                elif c_idx == len(matrix[0]) - 1:
                    matrix[r_idx][c_idx] = max(1, matrix[r_idx + 1][c_idx] - matrix[r_idx][c_idx])
                else:
                    matrix[r_idx][c_idx] = max(1, min(matrix[r_idx + 1][c_idx] - matrix[r_idx][c_idx], matrix[r_idx][c_idx + 1] - matrix[r_idx][c_idx]))
        return matrix[0][0]
