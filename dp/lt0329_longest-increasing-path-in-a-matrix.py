"""
dfs solution, using another matrix with same height and width to maintain the longest increasing path,
then loop through each elements to do the dp

time complexity: O(mn)
space complexity: O(mn)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        length_matrix = [[0 for j in range(0, n)] for i in range(0, m)]

        def dp(row, col):
            if length_matrix[row][col] != 0:
                return length_matrix[row][col]
            if (row + 1 >= m or matrix[row][col] > matrix[row + 1][col]) and (row -1 < 0 or matrix[row][col] > matrix[row -1][col]) and (col + 1 >= n or matrix[row][col] > matrix[row][col + 1]) and (col - 1 < 0 or matrix[row][col] > matrix[row][col -1]):
                length_matrix[row][col] = 1
                return 1
            else:
                length_matrix[row][col] =  max([dp(row - 1, col) if row -1 >= 0 and matrix[row][col] < matrix[row -1][col] else 0,
                                                dp(row + 1, col)  if row + 1 < m and matrix[row][col] < matrix[row +1][col] else 0,
                                                dp(row, col -1) if col - 1 >=0 and matrix[row][col] < matrix[row][col -1] else 0,
                                                dp(row, col + 1) if col + 1 < n and matrix[row][col] < matrix[row][col + 1] else 0]) + 1
                return length_matrix[row][col]
        for r_idx in range(0, len(matrix)):
            for c_idx in range(0, len(matrix[r_idx])):
                dp(r_idx, c_idx)
        ret = 0
        for r in length_matrix:
            for c in r:
                ret = max(ret, c)
        return ret