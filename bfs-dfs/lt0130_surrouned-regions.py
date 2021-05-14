"""
bfs solution
store all 'O's which are reachable to boundary, then set board to 'x', then set those cells back to 'o'

time complexity: O(m * n)
space complexity: O(# of Os)
"""
class Solution:
    def solve(self, board):
        r_num = len(board)
        c_num = len(board[0])
        o_set = set()

        for c_idx in range(0, c_num):
            if board[0][c_idx] == 'O':

                o_set.add((0, c_idx))
            if board[-1][c_idx] == 'O':

                o_set.add((r_num - 1, c_idx))

        for r_idx in range(0, r_num):
            if board[r_idx][0] == 'O':
                o_set.add((r_idx, 0))
            if board[r_idx][-1] == 'O':
                o_set.add((r_idx, c_num - 1))
        cur = o_set
        while cur:
            new_cur = set()
            for r_idx, c_idx in cur:
                board[r_idx][c_idx] = 'X'
            for r_idx, c_idx in cur:
                if r_idx - 1 >= 0 and board[r_idx - 1][c_idx] == 'O':
                    new_cur.add((r_idx - 1, c_idx))

                if r_idx + 1 < r_num and board[r_idx + 1][c_idx] == 'O':
                    new_cur.add((r_idx + 1, c_idx))
                if c_idx - 1 >= 0 and board[r_idx ][c_idx - 1] == 'O':
                    new_cur.add((r_idx, c_idx -1))
                if c_idx + 1 < c_num and board[r_idx][c_idx + 1] == 'O':
                    new_cur.add((r_idx, c_idx + 1))
            cur = new_cur
            o_set.update(new_cur)

        for r_idx in range(0, r_num):
            for c_idx in range(0, c_num):
                if (r_idx, c_idx) not in o_set:
                    board[r_idx][c_idx] = 'X'
                else:
                    board[r_idx][c_idx] = 'O'
