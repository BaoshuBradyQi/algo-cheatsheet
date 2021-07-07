"""
Q: given a matrix, 1 marked as valid path and 0 marked as obstacles; given two points, start and end
returns the longest valid path between two points (assume both points are reachable and there's path between them)

A: using dfs backtracking, for each step, mark current point as visited/obstacle,
and try to find the longest path from current point to destination

Time complexity: O(m * n * m * n), for each point, runs a backtracking dfs, m, n are the dimension of matrix
Spack complexity: O(m * n)
"""
def longestdis(matrix, start, end):

    moves = [0, 1, 0, -1, 0]
    def dfs(cur, dest, dis):
        r_idx, c_idx = cur
        if cur == dest:
            return dis
        ret = - float('INF')
        for i in range(4):
            new_r, new_c =  r_idx + moves[i], c_idx + moves[i + 1]
            if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c ] == 1:
                matrix[new_r][new_c] = 0
                ret = max(ret, dfs((new_r, new_c), dest, dis))
                matrix[new_r][new_c] = 1
        return ret + 1
    return dfs(start, end, 0)

matrix = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
]
assert(longestdis(matrix, (0, 0),  (5, 7)), 22)
assert(longestdis(matrix, (0, 0),  (0, 2)), 6)