"""
pretty standard dfs &memorization

check valid move and retrieve previously-went point

Time complexity: O(m * n) for m, n is the length and width of matrix, since all cells are visited once
Space complexity: O(m * n), for memorization
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        r_num = len(matrix)
        c_num = len(matrix[0])

        path_len = [[0 for _ in range(c_num)] for _ in range(r_num)]
        moves = [0, 1, 0, -1, 0]

        def dfs(r_idx, c_idx):

            if path_len[r_idx][c_idx] != 0:
                return path_len[r_idx][c_idx]
            prev = 0
            for i in range(4):
                new_r, new_c = r_idx + moves[i], c_idx + moves[i + 1]
                if 0 <= new_r <  len(matrix) and \
                        0 <= new_c < len(matrix[0]) and \
                        matrix[new_r][new_c] > matrix[r_idx][c_idx]:

                    prev = max(prev, dfs(new_r, new_c))
            ret = prev + 1
            path_len[r_idx][c_idx] = ret
            return ret

        for r_idx in range(r_num):
            for c_idx in range(c_num):
                dfs(r_idx, c_idx)

        return max( max(r) for r in path_len)
