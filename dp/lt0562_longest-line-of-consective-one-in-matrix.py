"""
simple dp solution, keep tracking the hoz, vert, diag and anti-diag length
using single line to store the result instead of entire matrix to save space

time complexity: O(m * n)
space complexity: O(m), m is the # of elements per line
"""
class Solution:
    def longestLine(self, matrix: List[List[int]]) -> int:
        ret = 0
        if not matrix or not matrix[0]:
            return ret

        # hoz, verti, dia, anti-dia
        line = list()
        for i in matrix[0]:

            if i == 1:
                if not line:
                    line.append((1, 1, 1, 1))
                else:
                    left = line[-1]
                    line.append((line[-1][0] + i, 1, 1, 1))
                ret = max(ret, max(line[-1]))
            else:
                line.append((0, 0, 0, 0))
        if len(matrix) > 1:
            for n_l in matrix[1:]:
                new_line = list()
                for idx, p in enumerate(n_l):
                    if p == 1:
                        if not new_line:

                            anti_diag = 0 if 1 == len(line) else line[1][3] + 1
                            new_line.append((1, line[0][1] + 1, 1, anti_diag))
                        else:
                            anti_diag = 0 if idx + 1 >= len(line) else line[idx + 1][3] + 1
                            new_line.append((new_line[-1][0] + 1,  line[idx][1] + 1, line[idx - 1][2] + 1, anti_diag))
                        ret = max(ret, max(new_line[-1]))

                    else:
                        new_line.append((0,0,0,0))
                line = new_line
        return ret

