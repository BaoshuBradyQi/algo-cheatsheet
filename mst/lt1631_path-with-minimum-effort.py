"""
straightforward dijkstra's algorithm, always explore the cell with minimal efforts
if reach the endpoint, then it must be using minimal efforts

time complexity: O(V + E logV), for V is #vertexes, E is #edges
space complexity: O(V)
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n_row = len(heights)
        n_col = len(heights[0])

        visited = set()
        boundary = list()
        moves = [0, 1, 0, -1, 0]
        ret = 0
        heappush(boundary, (0, 0, 0)) # efforts, r_idx, c_idx
        while boundary:
            eff, r_idx, c_idx = heappop(boundary)
            visited.add((r_idx, c_idx))
            ret = max(eff, ret)
            if r_idx == n_row - 1 and c_idx == n_col - 1:
                return ret
            for idx in range(4):
                new_r, new_c = r_idx + moves[idx], c_idx + moves[idx + 1]
                if 0  <= new_r < n_row and 0 <= new_c < n_col and (new_r, new_c) not in visited:
                    heappush(boundary, ( abs(heights[r_idx][c_idx] - heights[new_r][new_c]), new_r, new_c))