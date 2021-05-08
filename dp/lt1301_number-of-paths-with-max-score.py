"""
construct a matrix to record each step and to how many maximum solutions
for certain point, if up/left/diagonal are not reachable(# of solutions = 0), itself is not reachable

time complexity: O(n ^2)
space complexity: O(n ^ 2)

improvement: we can record line by line instead of entire matrix, which will cut space complexity to O(n)
"""
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        if not board:
            return[0, 0]
        matrix = [[(0, 0) for i in range(0, n)] for j in range(0, n)]
        matrix[0][0] = (0, 1)
        for r_idx, row in enumerate(board):
            for c_idx, col in enumerate(row):
                if col == "X":
                    matrix[r_idx][c_idx] = (0, 0)
                elif c_idx == 0 and r_idx > 0 and col != "S" and board[r_idx - 1][c_idx] != "X":
                    matrix[r_idx][c_idx] = (matrix[r_idx - 1][c_idx][0] + int(col), matrix[r_idx - 1][c_idx][1])
                elif r_idx == 0 and c_idx > 0 and col != "S" and board[r_idx][c_idx - 1] != "X":
                    matrix[r_idx][c_idx] = (matrix[r_idx][c_idx - 1][0] + int(col), matrix[r_idx][c_idx - 1][1])
                elif c_idx > 0 and r_idx > 0:
                    up = matrix[r_idx - 1][c_idx]
                    left = matrix[r_idx][c_idx - 1]
                    diagonal = matrix[r_idx - 1][c_idx - 1]
                    if up[1] == left[1] == diagonal[1] == 0:
                        continue
                    if col == "S":
                        col = 0
                    tmp_max = max([up[0], left[0], diagonal[0]])
                    cur = 0
                    if up[1] !=0 and up[0] == tmp_max:
                        cur += up[1]
                    if left[1] != 0 and left[0] == tmp_max:
                        cur += left[1]
                    if diagonal[1] != 0 and diagonal[0] == tmp_max:
                        cur += diagonal[1]
                    matrix[r_idx][c_idx] = (tmp_max + + int(col), cur)
        return [matrix[-1][-1][0], matrix[-1][-1][1] % (10 ** 9 + 7)]