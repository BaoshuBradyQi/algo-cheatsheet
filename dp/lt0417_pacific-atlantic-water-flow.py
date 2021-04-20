"""
ugly dfs solution
time complexity: O(mn)
space complexity: O(mn)
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pac_flow = [ [False for i in range(0, n)] for j in range(0, m)]
        at_flow = [ [False for i in range(0, n)] for j in range(0, m)]
        for r_idx, r in enumerate(pac_flow):
            for c_idx, c in enumerate(r):
                if r_idx == 0 or c_idx == 0:
                    pac_flow[r_idx][c_idx] = True
        for r_idx, r in enumerate(at_flow):
            for c_idx, c in enumerate(r):
                if r_idx == len(at_flow) - 1 or c_idx == len(r) - 1:
                    at_flow[r_idx][c_idx] = True
        def dp(matrix, row, col):
            if matrix[row][col]:
                dir_set = [(row -1, col), (row + 1, col), (row, col -1), (row, col + 1)]
                valid_dir = list(filter(lambda x: x[0] >= 0 and x[1] >=0 and x[0] < len(matrix) and x[1] < len(matrix[0]),dir_set ))
                for d in valid_dir:
                    if heights[d[0]][d[1]] >= heights[row][col] and not matrix[d[0]][d[1]]:
                        matrix[d[0]][d[1]] = True
                        dp(matrix, d[0], d[1])
        for r_idx, r in enumerate(pac_flow):
            for c_idx, c in enumerate(r):

                if r_idx ==0 or c_idx == 0:
                    dp(pac_flow, r_idx, c_idx)
        for r_idx, r in enumerate(at_flow):
            for c_idx, c in enumerate(r):

                if r_idx == len(at_flow) - 1 or c_idx == len(r) - 1:
                    dp(at_flow, r_idx, c_idx)
        ret = list()
        for r_idx in range(0, len(heights)):
            for c_idx in range(0, len(heights[r_idx])):
                if pac_flow[r_idx][c_idx] and at_flow[r_idx][c_idx]:
                    ret.append((r_idx, c_idx))
        return ret